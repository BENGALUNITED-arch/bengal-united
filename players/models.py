from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, help_text="e.g., Forward, Midfielder, Defender, Goalkeeper")
    jersey_number = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='players/', help_text="Upload a transparent PNG or high-quality photo")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide player from the website")
    
    class Meta:
        verbose_name_plural = "First Team Players"
        ordering = ['jersey_number']

    def __str__(self):
        return f"{self.jersey_number} - {self.name}"