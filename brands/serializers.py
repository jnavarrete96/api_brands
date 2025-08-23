# brands/serializers.py
from rest_framework import serializers
from .models import Brand, Owner

class BrandCreateSerializer(serializers.Serializer):
    brand_name = serializers.CharField(max_length=255)
    owner_name = serializers.CharField(max_length=255)

    def validate_brand_name(self, value):
        if Brand.objects.filter(name=value).exists():
            raise serializers.ValidationError("Ya existe una marca con ese nombre.")
        return value

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


class OwnerNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ["id", "name"]

class BrandListSerializer(serializers.ModelSerializer):
    owner = OwnerNestedSerializer(read_only=True)

    class Meta:
        model = Brand
        fields = ["id", "name", "owner"]


