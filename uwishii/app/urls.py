from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("menu",views.menu,name="menu"),
    path("about",views.about,name="about"),
    path("jobs",views.jobs,name="jobs"),
    path("contact",views.contact,name="contact"),
    path("shop",views.shop,name="shop"),
    path("orders",views.orders,name="orders"),
    path("cart",views.cart,name="cart"),
    path('add_status/', views.add_status, name='add_status'),
]
