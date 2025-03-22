import os
from django.db import models
from django.contrib.auth.models import User

def product_image_path(instance, filename):
    return os.path.join(f"products/{instance.category}/", filename)

class Products(models.Model):
    CATEGORY_CHOICES = [
        ("PC", "PC"),
        ("Laptop", "Laptop"),
        ("CPU", "CPU"),
        ("GPU", "GPU"),
        ("RAM", "RAM"),
        ("Storage", "Storage"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.CharField(max_length=150)
    photo = models.ImageField(upload_to=product_image_path) 
    photo_url = models.URLField(null=True, blank=True)
    
    cpu = models.CharField(max_length=150, null=True, blank=True)
    gpu = models.CharField(max_length=150, null=True, blank=True)
    storage = models.CharField(max_length=150, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} - {self.category} - {self.user.username}"
    
    class Meta():
        verbose_name_plural = 'Products'
    
    def price_with_currency(self):
            return f"{self.price} AZN"