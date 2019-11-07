from django.shortcuts import render


def index(request):
    template = 'index.html'
    return render(request, template)


def smartphones(request):
    template = 'smartphones.html'
    return render(request, template)


def empty_section(request):
    template = 'empty_section.html'
    return render(request, template)


def phone(request):
    template = 'phone.html'
    return render(request, template)


def cart(request):
    template = 'cart.html'
    return render(request, template)


def login(request):
    template = 'login.html'
    return render(request, template)
