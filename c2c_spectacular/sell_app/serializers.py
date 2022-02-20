from rest_framework import serializers
from .models import*


class Good_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('__all__')



class Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')
