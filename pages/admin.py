from django.contrib import admin
from django.utils.html import format_html
from .models import About, Facility, Program, JoinSection, JoinSectionPhoto

# --- PHOTO SLIDER INLINE ---
class JoinSectionPhotoInline(admin.TabularInline):
    model = JoinSectionPhoto
    extra = 1
    fields = ('image', 'image_preview', 'order')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: 60px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "No Image"

# --- JOIN SECTION SETTINGS ---
@admin.register(JoinSection)
class JoinSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [JoinSectionPhotoInline]
    
    # Ensures only one settings object exists
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True

# --- ABOUT SECTION ---
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True

# --- FACILITY ADMIN ---
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'name')
    search_fields = ('name',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 120px; height: 80px; object-fit: cover; border-radius: 6px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);" />', obj.image.url)
        return "No Image"

# --- PROGRAM ADMIN ---
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 120px; height: 70px; object-fit: cover; border-radius: 6px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);" />', obj.image.url)
        return "No Image"