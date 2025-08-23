# brands/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Brand
from .serializers import BrandCreateSerializer, BrandSerializer, BrandListSerializer
from .utils.responses import success_response, error_response

class BrandCreateView(APIView):
    def post(self, request):
        serializer = BrandCreateSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            brand = serializer.save()
            response_serializer = BrandSerializer(brand)
            return success_response(
                data=response_serializer.data,
                msg="Marca creada correctamente",
                status_code=status.HTTP_201_CREATED
            )
        except ValidationError as e:
            return error_response(
                errors=e.detail,
                msg="Error de validación",
                status_code=status.HTTP_409_CONFLICT
            )
        

class BrandListView(APIView):
    def get(self, request):
        brands = Brand.objects.select_related("owner").all()
        serializer = BrandListSerializer(brands, many=True)
        return success_response(data=serializer.data)
