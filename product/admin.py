from django.contrib import admin
from .models import Category, Product, Review
from mixins.admin_image_size import ImageSize

@admin.register(Category)
# Модель категории
class CategoryAdmin(admin.ModelAdmin, ImageSize):
    list_display = ['name', 'slug', 'image_show', 'created', 'uploaded']
    list_filter = ['created', 'uploaded']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Product)
# Модель товара
class ProductAdmin(admin.ModelAdmin, ImageSize):
    list_display = ['name', 'slug', 'image_show', 'price', 'available', 'created', 'uploaded']
    list_filter = ['available', 'created', 'uploaded']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name', )}

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'text', 'date', 'author']

admin.site.register(Review, ReviewAdmin)