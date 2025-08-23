# brands/views.py
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import Brand
from .serializers import BrandCreateSerializer, BrandSerializer, BrandListSerializer, BrandUpdateSerializer
from .utils.responses import success_response, error_response

class BrandCreateView(APIView):
    @extend_schema(
        summary="Crear una nueva marca",
        description="Crea una marca asociada a un titular. Si el titular no existe, se crea automáticamente.",
        request=BrandCreateSerializer,
        responses={201: BrandSerializer, 409: None},
        tags=["Marcas"]
    )
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
    @extend_schema(
        summary="Listar todas las marcas",
        description="Devuelve una lista completa de marcas registradas junto con su titular.",
        responses={200: BrandListSerializer(many=True)},
        tags=["Marcas"]
    )
    def get(self, request):
        brands = Brand.objects.select_related("owner").all()
        serializer = BrandListSerializer(brands, many=True)
        return success_response(data=serializer.data)
    

class BrandByOwnerView(APIView):
    @extend_schema(
        summary="Listar marcas por titulares",
        description="Filtra marcas cuyo nombre de titular contiene el texto proporcionado.",
        parameters=[
            OpenApiParameter(
                name="owner",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Texto parcial del nombre del titular"
            )
        ],
        responses={200: BrandListSerializer(many=True)},
        tags=["Marcas"]
    )
    def get(self, request):
        owner_query = request.query_params.get("owner", "").strip()
        brands = Brand.objects.select_related("owner")

        if owner_query:
            brands = brands.filter(owner__name__icontains=owner_query)

        serializer = BrandListSerializer(brands, many=True)
        return success_response(data=serializer.data)
    

class BrandDeleteView(APIView):
    @extend_schema(
        summary="Eliminar una marca",
        description="Elimina una marca por su ID. Si el titular asociado no tiene más marcas después de la eliminación, también se elimina automáticamente.",
        parameters=[
            OpenApiParameter(
                name="brand_id",
                type=int,
                location=OpenApiParameter.PATH,
                description="ID de la marca a eliminar"
            )
        ],
        responses={200: None, 404: None},
        tags=["Marcas"]
    )
    def delete(self, request, brand_id):
        try:
            brand = Brand.objects.select_related("owner").get(id=brand_id)
            owner = brand.owner
            brand.delete()

            # Verificar si el owner tiene otras marcas
            if not owner.brands.exists():
                owner.delete()

            return success_response(msg="Marca eliminada correctamente")
        except Brand.DoesNotExist:
            return error_response(msg="Marca no encontrada", status_code=status.HTTP_404_NOT_FOUND)
    
class BrandUpdateView(APIView):
    @extend_schema(
        summary="Actualizar marca",
        description="Actualiza el nombre o estado de una marca por su ID. Los campos son opcionales.",
        request=BrandUpdateSerializer,
        responses={200: BrandSerializer, 400: None, 404: None},
        tags=["Marcas"]
    )
    def patch(self, request, brand_id):
        try:
            brand = Brand.objects.get(id=brand_id)
        except Brand.DoesNotExist:
            return error_response(msg="Marca no encontrada", status_code=status.HTTP_404_NOT_FOUND)

        serializer = BrandUpdateSerializer(data=request.data, context={"brand_id": brand_id})
        if serializer.is_valid():
            updated_brand = serializer.update(brand, serializer.validated_data)
            response_data = BrandSerializer(updated_brand).data
            return success_response(data=response_data, msg="Marca actualizada correctamente")
        else:
            return error_response(errors=serializer.errors, msg="Error de validación", status_code=status.HTTP_400_BAD_REQUEST)
