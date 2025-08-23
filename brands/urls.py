from django.urls import path
from .views import BrandCreateView, BrandListView, BrandByOwnerView, BrandDeleteView, BrandUpdateView

urlpatterns = [
    path('brand', BrandCreateView.as_view(), name='brand-create'),
    path('brands', BrandListView.as_view(), name='brand-list'),
    path('brands/by-owner', BrandByOwnerView.as_view(), name='brand-by-owner'),
    path('brand/<int:brand_id>', BrandDeleteView.as_view(), name='brand-delete'),
    path('brand/<int:brand_id>/update', BrandUpdateView.as_view(), name='brand-update'),
]