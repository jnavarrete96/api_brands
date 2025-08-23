from django.urls import path
from .views import BrandCreateView, BrandListView, BrandByOwnerView

urlpatterns = [
    path('brand', BrandCreateView.as_view(), name='brand-create'),
    path('brands', BrandListView.as_view(), name='brand-list'),
    path('brands/by-owner', BrandByOwnerView.as_view(), name='brand-by-owner'),
]