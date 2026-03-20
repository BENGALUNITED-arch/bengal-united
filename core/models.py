from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="Bengal United")
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    contact_email = models.EmailField(default="info@bengalunited.com")
    contact_phone = models.CharField(max_length=20, default="+91 98765 43210")
    whatsapp_number = models.CharField(max_length=20, help_text="Include country code, e.g., 919876543210")
    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    
    class Meta:
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Website Settings"

class HeroSlide(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='hero/')
    cta_text = models.CharField(max_length=50, default="Join Academy")
    cta_link = models.CharField(max_length=200, default="#programs")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Hero Sliders"

    def __str__(self):
        return self.title