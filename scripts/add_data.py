import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
import django
django.setup()

import json as json_lib
from app.models.products import Products
from django.contrib.auth.models import User

user = User.objects.get(username='admin')

def add_product():
    with open('scripts/ComputerPRoducts.json', 'r', encoding='utf-8') as f:
        read = f.read()  
        data = json_lib.loads(read)['Data']  
        for product_data in data:
            photoe = product_data.get('Photo', '')  
            title = product_data.get('Title', '')  
            descriptione = product_data.get('Description', '') 
            pricee = product_data.get('Price', '').replace(" ", "")
            category = product_data.get('Category', '').replace(" ", "")
            try:
                pricee = int(pricee)  
            except ValueError:
                pricee = 0  

            product = Products(
                user=user,
                category=category,  
                brand=title,
                price=pricee,
                description=descriptione,
                photo_url=photoe
            )
            product.save()  

add_product()
