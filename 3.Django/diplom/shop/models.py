from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название товара')
    content = models.TextField(max_length=2000, verbose_name='Описание товара')
    price = models.PositiveIntegerField(blank=True, verbose_name='Цена')
    image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Изображение')
    published = models.DateField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 related_name='product')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='Транслит')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название категории')
    index = models.PositiveIntegerField(verbose_name='Приоритет')
    rubric = models.ForeignKey('Rubric', related_name='category', verbose_name='Рубрика',
                               on_delete=models.PROTECT)
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='Транслит')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['index', 'name']


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название раздела')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    published = models.DateField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    products = models.ManyToManyField(Product,
                                      related_name='articles',
                                      verbose_name='Список продуктов')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published']


class ArticlesProduct(models.Model):
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.product.name


class Order(models.Model):
    user = models.ForeignKey(User, related_name='order_list', on_delete=models.PROTECT, verbose_name='Пользователь')
    date_created = models.DateField(auto_now_add=True, db_index=True, verbose_name='Дата создания')

    class Meta:
        ordering = ('-date_created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT, verbose_name='Товар')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
