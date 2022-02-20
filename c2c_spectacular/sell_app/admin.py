from django.contrib import admin

from django.contrib import admin
from .models import*



class My_User_Admin(admin.ModelAdmin):
    class Meta:
        list_display = ('username','surname', 'phone_number',)
        list_display_links = ('username','surname', 'phone_number')
        search_fields = ('username','surname','phone_number',)


admin.site.register(My_User, My_User_Admin)

class Customer_Admin(admin.ModelAdmin):
    class Meta:
        list_display = ('name', 'auth_key', 'phone_number',)
        list_display_links = ('name', 'auth_key', 'phone_number')
        search_fields = ('name', 'auth_key', 'phone_number')

admin.site.register(Customer, Customer_Admin)


class Good_Admin(admin.ModelAdmin):
    class Meta:
        list_display = ('customer','code','description','quantity')
        list_display_links = ('customer','code',)
        search_fields = ('customer','code','description','quantity')
        list_filter = ('customer','code',)
admin.site.register(Good, Good_Admin)


