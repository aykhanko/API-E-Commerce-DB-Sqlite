from django.contrib import admin
from app.models.profile import Profile
from app.models.products import Products

admin.site.register(Profile)
admin.site.register(Products)