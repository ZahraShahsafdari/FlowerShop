from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.product, name='product'),
    path('store/', views.store, name='store'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('to-bank/<int:order_id>/', views.to_bank, name='to_bank'),
    path('callback/', views.callback, name='callback'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('search/', views.search, name='search'),]