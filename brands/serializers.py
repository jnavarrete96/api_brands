# brands/serializers.py
from rest_framework import serializers
from .models import Brand, Owner

class BrandCreateSerializer(serializers.Serializer):
    brand_name = serializers.CharField(max_length=255)
    owner_name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        owner, _ = Owner.objects.get_or_create(name=validated_data["owner_name"])
        brand = Brand.objects.create(
            name=validated_data["brand_name"],
            owner=owner,
        )
        return brand
    

class BrandSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source="owner.name", read_only=True)

    class Meta:
        model = Brand
        fields = ["name", "status", "owner_name"]

