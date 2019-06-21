import pytest
import json

from rest_framework import status
from .factories import ProductCategoryFactory, ProductFactory


@pytest.fixture
def category():
    return ProductCategoryFactory()


@pytest.mark.django_db
def test_endpoint(client, category):
    response = client.get(
        f'/api/v1/categories/{category.id}', follow=True)
    content = json.loads(response.content)
    assert content['name'] == category.name
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_all_categories(client):
    response = client.get(
        f'/api/v1/categories/'
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_single_category(client, category):
    response = client.post(
        f'/api/v1/categories/'
    )
    assert response.status_code == status.HTTP_200_OK
