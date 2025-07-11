from django.urls import path
from . import views
from django.db import models
from django.contrib.auth import views as auth_views

app_name = 'store'

urlpatterns = [
    path('', views.package_list, name='package_list'),
    path('<int:pk>/', views.package_detail, name='package_detail'),
    path('buy/<int:pk>/', views.purchase_package, name='purchase_package'),
    path('my-purchases/', views.my_purchases, name='my_purchases'),
    path('oriental-music/', views.oriental_music_list, name='oriental_music_list'),
    path('start-purchase/<int:pk>/', views.start_purchase, name='start_purchase'),
    path('register/', views.register_view, name='register_view'),
    path('start-payment/<int:pk>/', views.start_payment, name='start_payment'),
    path('verify-payment/', views.verify_payment, name='verify_payment'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

]


