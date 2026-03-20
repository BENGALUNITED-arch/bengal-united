from django.contrib import admin
from django.utils.html import format_html
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Using name or title depending on what you named it in your models.py!
    list_display = ('image_preview', '__str__') 
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto; object-fit: contain; background: #111827; padding: 5px; border-radius: 6px;" />', obj.image.url)
        return "No Image"
    
    image_preview.short_description = 'Preview'