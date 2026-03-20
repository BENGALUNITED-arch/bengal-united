from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'jersey_number', 'position', 'is_active')
    list_editable = ('is_active',) # Lets admin click a switch to hide players instantly
    search_fields = ('name', 'position')
    list_filter = ('position', 'is_active')