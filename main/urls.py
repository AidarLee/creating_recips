from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #Main page index
    path('', views.index, name='index'),

    #Admin urls
    path('accounts/login/', views.login_page, name='login_page'),
    path('accounts/login/success/', views.authorization, name='authorizate'),
    path('accounts/logout/', views.logout_page, name = 'logout_page'),
    path(r'admin-panel/profile/update/^', views.ProfileUpdateView.as_view(), name = 'update_profile'),
    path(r'admin-panel/profile/update/^/change_password/', views.ChangePasswordView.as_view(), name = 'change_password'),
    path('admin-panel/main/', views.AdminMain.as_view(), name='admin_panel'),


    #Client urls
    path('about', views.about, name='about-us'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('meels', views.meels, name='meels'),
    path('milks', views.milks, name='milks'),
    path('bakery', views.bakery, name='bakery'),
    path('list', views.list, name='list-of-products')
]