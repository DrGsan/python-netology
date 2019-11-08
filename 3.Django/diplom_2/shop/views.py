from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

from .models import Article, Category, Product, Order, OrderItem


class ArticleView(ListView):
    template_name = 'shop/index.html'
    model = Article

    def post(self, request, *args, **kwargs):
        article_list = Article.objects.all()
        product = request.POST.get('product')
        if 'cart' in request.session:
            if product in request.session['cart']:
                request.session['cart'][product] += 1
                request.session.modified = True
            else:
                request.session['cart'][product] = 1
                request.session.modified = True
        else:
            request.session['cart'] = {product: 1}
        return render(request, 'shop/index.html', {'article_list': article_list})


class CategoryView(DetailView):
    template_name = 'shop/category.html'
    model = Category
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_list = list(context['category'].product.all())

        paginator = Paginator(product_list, 3)
        page = self.request.GET.get('page')

        context['product_list'] = paginator.get_page(page)

        if page:
            context['current_page'] = paginator.page(page).number
        else:
            context['current_page'] = paginator.page(1).number
        if paginator.get_page(page).has_previous():
            context['prev_page_url'] = f'?page={paginator.get_page(page).previous_page_number()}'
        else:
            context['prev_page_url'] = None
        if paginator.get_page(page).has_next():
            context['next_page_url'] = f'?page={paginator.get_page(page).next_page_number()}'
        else:
            context['next_page_url'] = None

        return context

    def post(self, request, *args, **kwargs):        
        current_page = request.POST.get('current_page')                
        product = request.POST.get('product')
        if 'cart' in request.session:
            if product in request.session['cart']:
                request.session['cart'][product] += 1
                request.session.modified = True
            else:
                request.session['cart'][product] = 1
                request.session.modified = True
        else:
            request.session['cart'] = {product: 1}
        return redirect(f'http://127.0.0.1:8000/shop/category/noutbuki/?page={current_page}')
    
    
class ProductView(DetailView):
    template_name = 'shop/product.html'
    model = Product

    def post(self, request, *args, **kwargs):
        slug = kwargs['slug']
        product = Product.objects.get(slug=slug)
        if 'cart' in request.session:
            if slug in request.session['cart']:
                request.session['cart'][slug] += 1
                request.session.modified = True
            else:
                request.session['cart'][slug] = 1
                request.session.modified = True
        else:
            request.session['cart'] = {slug: 1}
        return render(request, 'shop/product.html', {'product': product})


def cart(request):
    cart_list = []
    message = ''
    if not request.session.get('cart'):
        message = 'Корзина пуста'
        return render(request, 'shop/cart.html', {'message': message})

    for slug, value in request.session['cart'].items():
        product = Product.objects.get(slug=slug)
        cart_list.append((product, value))
    counter = len(cart_list)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        for product, quantity in cart_list:
            OrderItem.objects.create(order=order,
                                     product=product,
                                     price=product.price,
                                     quantity=quantity)
        del request.session['cart']
        cart_list = []
        counter = None
        message = 'Заказ оформлен'
    return render(request, 'shop/cart.html', {'cart_list': cart_list, 'counter': counter, 'message': message})

