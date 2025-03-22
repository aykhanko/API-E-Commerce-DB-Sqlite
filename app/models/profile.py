from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?[0-9\s\(\)\-]+$', message="Nömrəni düzgün daxil edin: XXX-XXX-XXXX)") 
    phone = models.CharField(validators=[phone_regex], max_length=30, null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    class Meta():
        verbose_name_plural = 'Profiles'

class UserProducts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    