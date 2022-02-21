from django.urls import*
from django.contrib.auth.views import*
from .views import*

from rest_framework.schemas import get_schema_view

from django.views.generic import TemplateView







app_name = 'sell_app'


urlpatterns = [


    path('api/schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
    #_______ALL______SECTION__________
    path('api/customers/',api_customers),
    path('api/goods/',api_goods),

    #_______DETAIL___SECTION__________
    path('api/customer/<int:pk>/',api_customer_detail),
    path('api/good/<int:pk>/',api_goods_detail),
    #--------------------------------------------
    path('api/docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'api_schema'}
    ), name='swagger-ui'),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
]

'''http://127.0.0.1:8000/sell_app/api_schema/'''
'''http://127.0.0.1:8000/sell_app/api/docs/'''
'''http://127.0.0.1:8000/sell_app/api/docs/'''
