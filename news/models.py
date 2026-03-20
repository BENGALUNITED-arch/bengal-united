from django.db import models
from django.utils import timezone

class News(models.Model):
    CATEGORY_CHOICES = [
        ('MATCH', 'Match Report'),
        ('ACADEMY', 'Academy'),
        ('CLUB', 'Club News'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='CLUB')
    image = models.ImageField(upload_to='news/')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True) # Kept intact
    is_published = models.BooleanField(default=True)

    # --- EXTENDED FUNCTIONALITY ---
    publish_date = models.DateTimeField(
        default=timezone.now,
        help_text="Select a past date to backdate, or a future date to schedule."
    )
    last_updated = models.DateTimeField(
        default=timezone.now,
        help_text="Manually click 'Today' and 'Now' when making major edits to push to the top."
    )

    class Meta:
        verbose_name_plural = "Latest News"
        ordering = ['-publish_date']  # Changed to sort by the new publish date

    def __str__(self):
        return self.title