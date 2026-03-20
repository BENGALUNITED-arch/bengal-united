from django.contrib import admin
from .models import SiteSettings, HeroSlide

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    # This prevents the client from creating multiple settings pages
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')