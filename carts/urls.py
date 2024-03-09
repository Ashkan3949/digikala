from django.urls import path
from . import views

urlpatterns = [
    path('', views.carts_summery, name='cart_summery'),
    path('ass/', views.carts_add, name='cart_add'),
    path('delete/', views.carts_delete, name='cart_delete0'),
    path('update/', views.carts_update, name='cart_update'),

]