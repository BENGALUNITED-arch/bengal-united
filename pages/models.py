from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200, default="About Bengal United")
    history = models.TextField(help_text="The founding story and history of the club.")
    mission = models.TextField(help_text="What is the club's main goal?")
    vision = models.TextField(help_text="Where is the club going in the future?", blank=True, null=True)
    image = models.ImageField(upload_to='about/', help_text="Cover image for the About section")

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return "Club About Page Settings"


class Facility(models.Model):
    name = models.CharField(max_length=150, help_text="e.g., High-Performance Gym, Main Pitch")
    description = models.TextField(help_text="Details about the equipment, size, or usage.")
    image = models.ImageField(upload_to='facilities/', help_text="A high-quality photo of the facility.")
    
    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"

    def __str__(self):
        return self.name


class Program(models.Model):
    title = models.CharField(max_length=200, help_text="e.g., Elite Youth Academy, Summer Camp")
    description = models.TextField(help_text="Details about what the program offers.")
    image = models.ImageField(upload_to='programs/', help_text="Upload an action shot for this program")
    is_active = models.BooleanField(default=True, help_text="Uncheck to temporarily hide this from the website")

    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programs"

    def __str__(self):
        return self.title


# ====== UPGRADED JOIN SECTION MODELS ======

class JoinSection(models.Model):
    title = models.CharField(max_length=200, default="JOIN THE NEXT GENERATION OF CHAMPIONS")
    description = models.TextField(default="Spots for our upcoming elite trials are strictly limited. Secure your place now and start your journey.")
    button_text = models.CharField(max_length=50, default="MESSAGE US ON WHATSAPP")
    
    class Meta:
        verbose_name = "Join Section Settings"
        verbose_name_plural = "Join Section Settings"

    def __str__(self):
        return "Join Section Text & Settings"

class JoinSectionPhoto(models.Model):
    """Allows uploading multiple background photos for a slider effect"""
    join_section = models.ForeignKey(JoinSection, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='join_section_slider/', help_text="Upload photos for the background slider")
    order = models.PositiveIntegerField(default=0, help_text="Order in which photos appear")

    class Meta:
        ordering = ['order']
        verbose_name = "Join Section Background Photo"
        verbose_name_plural = "Join Section Background Photos"