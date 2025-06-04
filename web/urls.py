from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blogs/", views.blog, name="blog"),
    path("products/", views.product, name="product"),
    path("contact/", views.contact, name="contact"),

    path("wish-list/", views.wish_list, name="wish_list"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout",)
]