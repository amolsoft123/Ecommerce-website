from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','age','address']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','shape','size','image','location','price']

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['id','product_id','user_id']
