from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductCategory
from .serializer import (
    ProductSerializer,
    ProductCategorySerializer,
)


@api_view(["GET", "DELETE", "PUT"])
def get_delete_update_product_category(request, pk):
    try:
        category = ProductCategory.objects.get(pk=pk)
    except ProductCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single category
    if request.method == "GET":
        serializer = ProductCategorySerializer(category)
        return Response(serializer.data)
    # delete a single category
    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single puppy
    elif request.method == "PUT":
        serializer = ProductCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def get_post_product_category(request):
    # get all categories
    if request.method == "GET":
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data)
    # insert a new record for a category
    elif request.method == "POST":
        data = {
            'id': request.data.get('id'),
            'name': request.data.get('name'),
            'description': request.data.get('description')
        }
        serializer = ProductCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
