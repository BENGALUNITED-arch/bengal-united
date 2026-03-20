from django.contrib import admin
from .models import Album, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    # Shows the new fields in the dashboard
    list_display = ('title', 'category', 'date_created', 'is_active')
    list_filter = ('category', 'is_active')
    
    # Lets you change category and hide/show WITHOUT clicking into the album!
    list_editable = ('category', 'is_active') 
    
    inlines = [PhotoInline]