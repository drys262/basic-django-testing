from django.urls import path
from .views import (
    get_delete_update_product_category,
    get_post_product_category,
)

urlpatterns = [
    # path('', index, name="index"),
    # path('<int:category_id>/', detail, name="detail"),
    # path('<int:category_id>/results', results, name="results"),

    path(
        'categories/',
        get_post_product_category,
        name="get_post_product_category"
    ),

    path(
        'categories/<str:pk>/',
        get_delete_update_product_category,
        name="get_delete_update_product_category"
    ),


]
