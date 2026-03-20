from django.db import models

class Trophy(models.Model):
    name = models.CharField(max_length=200, help_text="e.g., Bengal State League")
    year = models.CharField(max_length=4, help_text="e.g., 2024")
    description = models.TextField(blank=True, help_text="Short detail about the victory.")
    image = models.ImageField(upload_to='trophies/', help_text="Upload a picture of the cup/shield")

    class Meta:
        verbose_name_plural = "Trophies"
        ordering = ['-year'] # Sorts newest trophies first

    def __str__(self):
        return f"{self.name} ({self.year})"