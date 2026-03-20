from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(help_text="Detailed product information")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in INR")
    image = models.ImageField(upload_to='shop/products/')
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name