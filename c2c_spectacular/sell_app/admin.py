from django.contrib import admin

from django.contrib import admin
from .models import*



class Customer_Admin(admin.ModelAdmin):
    class Meta:
        list_display = ('username', 'user_type','phone_number',)
        list_display_links = ('username', 'user_type','phone_number')
        search_fields = ('user_type','username','phone_number',)
        list_filter = ('username', 'phone_number',)

admin.site.register(Customer, Customer_Admin)


class Good_Admin(admin.ModelAdmin):
    class Meta:
        list_display = ('customer','code','description','quantity')
        list_display_links = ('customer','code',)
        search_fields = ('customer','code','description','quantity')
        list_filter = ('customer','code',)
admin.site.register(Good, Good_Admin)


