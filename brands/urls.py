from django.urls import path
from .views import BrandCreateView

urlpatterns = [
    path('brands/', BrandCreateView.as_view(), name='brand-create'),
]