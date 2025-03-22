from django.urls import path
from app.api import views

################################################SWAGGER#####################################################################
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce",
        default_version='v1',
        description="Users doing something",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

################################################################################################################################

urlpatterns = [
    path('profile/<str:user__username>/', views.ProfileDetailsAPIView.as_view(), name='profile_detail'),

    path("products/", views.ProductsAPIView.as_view(), name="product_list"),
    path("products/add/", views.UserCreateProductsAPIView.as_view(), name="product_add"),
    path("user/products/", views.UserProducts.as_view(), name="user_products"),
    path("user/products/<int:pk>/", views.UserProductsDetails.as_view(), name="user_products_detail"),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]
