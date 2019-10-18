from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    is_review_exist = False
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = product.review.all()

    if request.method == 'GET':
        if not request.session['reviewed_products']:
            request.session['reviewed_products'] = list()
        if product.id in request.session['reviewed_products']:
            is_review_exist = True

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(text=form.cleaned_data['text'], product=product)
            review.save()
            request.session.modified = True
            if product.id not in request.session['reviewed_products']:
                request.session['reviewed_products'].append(product.id)
    else:
        form = ReviewForm()

    print(request.session['reviewed_products'])
    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
        'is_review_exist': is_review_exist}

    return render(request, template, context)
