from django.contrib import admin
from .models import Product, Article, Category, ArticlesProduct, Rubric, Order, OrderItem


class ArticlesProductInline(admin.TabularInline):
    model = ArticlesProduct


class CategoryInline(admin.TabularInline):
    model = Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    exclude = ['products']
    inlines = [ArticlesProductInline]
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date_created']
    list_filter = ['date_created']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
