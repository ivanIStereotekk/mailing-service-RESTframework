from django.urls import path,include

from.views import*
from django.contrib.auth.views import*
from .views import*

app_name = 'sell_app'


urlpatterns = [
    #_______ALL______SECTION__________
    path('api/customers/',api_customers),
    path('api/goods/',api_goods),

    #_______DETAIL___SECTION__________
    path('api/customer/<int:pk>/',api_customer_detail),
    path('api/good/<int:pk>/',api_goods_detail),
    ]
