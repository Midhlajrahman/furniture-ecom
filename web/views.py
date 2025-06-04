from django.shortcuts import render


def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)

def about(request):
    context = {
        "is_about":True
    }
    return render(request, "web/about.html", context)

def blog(request):
    context = {
        "is_blog":True
    }
    return render(request, "web/blog.html", context)

def product(request):
    context = {
        "is_product":True
    }
    return render(request, "web/product.html", context)

def contact(request):
    context = {
        "is_contact":True
    }
    return render(request, 'web/contact.html', context)


def wish_list(request):
    return render(request, 'web/wish-list.html')

def cart(request):
    return render(request, "web/cart.html")

def checkout(request):
    return render(request, "web/checkout.html")