from django.urls import path
from .views import BrandCreateView, BrandListView, BrandByOwnerView, BrandDeleteView

urlpatterns = [
    path('brand', BrandCreateView.as_view(), name='brand-create'),
    path('brands', BrandListView.as_view(), name='brand-list'),
    path('brands/by-owner', BrandByOwnerView.as_view(), name='brand-by-owner'),
    path('brand/<int:brand_id>', BrandDeleteView.as_view(), name='brand-delete'),
]