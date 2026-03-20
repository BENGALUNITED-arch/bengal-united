from django.db import models
from django_resized import ResizedImageField # Import the compressor

class Album(models.Model):
    CATEGORY_CHOICES = [
        ('Match Day', 'Match Day'),
        ('Practice', 'Practice'),
        ('Behind The Scenes', 'Behind The Scenes'),
    ]
    
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Match Day')
    
    # Optimized Cover Image
    cover_image = ResizedImageField(
        size=[800, 500], 
        quality=75, 
        upload_to='gallery/covers/', 
        force_format='WebP', 
        blank=True, 
        null=True
    )
    
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this album from the website")

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    
    # Optimized Gallery Photos: Automatically shrinks and converts to WebP
    image = ResizedImageField(
        size=[1200, None], # Max width 1200px, height scales automatically
        quality=75, 
        upload_to='gallery/photos/', 
        force_format='WebP'
    )