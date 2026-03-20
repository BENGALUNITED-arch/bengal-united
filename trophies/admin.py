from django.contrib import admin
from django.utils.html import format_html
from .models import Trophy

@admin.register(Trophy)
class TrophyAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'name', 'year')
    list_display_links = ('name',)
    search_fields = ('name', 'year')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:100%; height:200px; object-fit:contain; filter: drop-shadow(0 10px 8px rgba(250, 204, 21, 0.2));" />', obj.image.url)
        return format_html('<div style="height:200px; display:flex; align-items:center; justify-content:center; color:#6B7280;"><i class="fas fa-trophy fa-3x"></i></div>')
    
    image_preview.short_description = 'Silverware'