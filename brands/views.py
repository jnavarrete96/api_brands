# brands/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Brand
from .serializers import BrandCreateSerializer, BrandSerializer, BrandListSerializer

class BrandCreateView(APIView):
    def post(self, request):
        serializer = BrandCreateSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            brand = serializer.save()
            response_serializer = BrandSerializer(brand)
            return Response(
                {
                    "msg": "creado correctamente",
                    "data": response_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        except ValidationError as e:
            return Response(
                {"error": e.detail},
                status=status.HTTP_409_CONFLICT,
            )
        

class BrandListView(APIView):
    def get(self, request):
        brands = Brand.objects.select_related("owner").all()
        serializer = BrandListSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
