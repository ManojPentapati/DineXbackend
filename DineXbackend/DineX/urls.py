from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('DineXlogin'), name='home'),
    path('homepage/', views.homepage_view, name='homepage'),
    path('products/', views.product_list, name='product-list'),
    path('products/cards/', views.product_cards_view, name='product-cards'),
    path('products/create/', views.product_create, name='product-create'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('products/<int:pk>/update/', views.product_update, name='product-update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product-delete'),
    path('login/', views.login_view, name='DineXlogin'),
    path('signup/', views.signup_view, name='DineXsignup'),
    path('logout/', views.logout_view, name='logout'),
]