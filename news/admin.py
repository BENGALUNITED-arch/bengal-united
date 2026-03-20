from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publish_date', 'last_updated', 'is_published')
    list_filter = ('category', 'is_published', 'publish_date')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)