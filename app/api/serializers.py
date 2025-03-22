from rest_framework import serializers
from app.models.profile import Profile
from app.models.products import Products

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta():
        model = Profile
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer(source="user.profile", read_only=True)
    price_with_currency = serializers.SerializerMethodField()

    class Meta():
        model = Products
        fields = ['user_profile', 'id', 'category', 'brand', 'price', 'price_with_currency', 'description', 'photo', 'photo_url', 'cpu', 'gpu', 'storage', 'created_at', 'updated_at']
    

    def get_price_with_currency(self, obj):
        return f"{obj.price} AZN"