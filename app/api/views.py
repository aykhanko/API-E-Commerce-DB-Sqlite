from rest_framework import generics
from rest_framework.exceptions import ValidationError

from app.models.profile import Profile
from app.models.products import Products
from app.api.serializers import ProfileSerializer, ProductsSerializer

from app.api.permissions import OwnOrNot
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey

from app.api.pagination import ProductPagination

class ProfileDetailsAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, OwnOrNot] 
    serializer_class = ProfileSerializer
    lookup_field = 'user__username'

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
        
class ProductsAPIView(generics.ListAPIView):
    permission_classes = [HasAPIKey]
    queryset = Products.objects.all().order_by('-created_at')
    serializer_class = ProductsSerializer
    pagination_class = ProductPagination

class UserCreateProductsAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return Products.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        if self.request.user.is_staff:  
            serializer.save(user=self.request.user)
            return
        
        user_products_count = Products.objects.filter(user=self.request.user).count()
        profile = self.request.user.profile
        if not profile.phone or not profile.mail or not profile.date_of_birth:
            raise ValidationError("To add a product, you must fill in your phone number, email address, and date of birth in your profile.")

        if user_products_count >= 3:
            raise ValidationError("You can add a maximum of 3 products.")

        serializer.save(user=self.request.user)

class UserProducts(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return Products.objects.filter(user=self.request.user).order_by('-created_at')
    
class UserProductsDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return Products.objects.filter(user=self.request.user)

