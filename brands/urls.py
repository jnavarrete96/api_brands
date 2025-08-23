from django.urls import path
from .views import BrandCreateView, BrandListView

urlpatterns = [
    path('brand', BrandCreateView.as_view(), name='brand-create'),
    path('brands', BrandListView.as_view(), name='brand-list'),
]