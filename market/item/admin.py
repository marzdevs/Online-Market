from django.contrib import admin

# looks for  Category in models.py
from .models import Category, Item

# Register your models here.

# creates a database table for category
admin.site.register(Category)
admin.site.register(Item)