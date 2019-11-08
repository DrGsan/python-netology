from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def cart(request):
    template_name = 'cart.html'
    return render(request, template_name)


def smartphones(request):
    template_name = 'smartphones.html'
    return render(request, template_name)
