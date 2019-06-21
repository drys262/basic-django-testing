import json
import uuid


from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Product, ProductCategory
from ..serializer import (
    ProductSerializer,
    ProductCategorySerializer,
)

# initialize the APIClient app
client = Client()


class GetAllCategoriesTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        ProductCategory.objects.create(
            id=uuid.uuid4(),
            name="Test Category 1",
            description="Test Category 1 Description")
        ProductCategory.objects.create(
            id=uuid.uuid4(),
            name="Test Category 2",
            description="Test Category 2 Description")
        ProductCategory.objects.create(
            id=uuid.uuid4(),
            name="Test Category 3",
            description="Test Category 3 Description")
        ProductCategory.objects.create(
            id=uuid.uuid4(),
            name="Test Category 4",
            description="Test Category 4 Description")

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_product_category'))
        # get data from db
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleCategoryTest(TestCase):
    """ Test module for GET single category API """

    def setUp(self):
        self.cat1 = ProductCategory.objects.create(
            id=uuid.uuid4(),
            name="Cat 1",
            description="Cat 1 Desc"
        )
        self.cat2 = ProductCategory.objects.create(
            id=uuid.uuid4(),
            name="Cat 2",
            description="Cat 2 Desc"
        )
        self.cat3 = ProductCategory.objects.create(
            id=uuid.uuid4(),
            name="Cat 3",
            description="Cat 3 Desc"
        )
        self.cat4 = ProductCategory.objects.create(
            id=uuid.uuid4(),
            name="Cat 4",
            description="Cat 4 Desc"
        )

    def test_get_valid_single_category(self):
        pk = self.cat1.pk
        response = client.get(
            reverse('get_delete_update_product_category',
                    kwargs={'pk': pk}),
        )
        cat1 = ProductCategory.objects.get(pk=pk)
        serializer = ProductCategorySerializer(cat1)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_category(self):
        response = client.get(
            reverse('get_delete_update_product_category',
                    kwargs={'pk': uuid.uuid4()}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateCategoryTest(TestCase):
    """ Test module for inserting a new category """

    def setUp(self):
        self.valid_payload = {
            'id': str(uuid.uuid4()),
            'name': 'Test Category',
            'description': 'Test Category Desc'
        }
        self.invalid_payload = {
            'id': str(uuid.uuid4()),
            'name': '',
            'description': 'Test Category Desc'
        }

    def test_create_valid_category(self):
        response = client.post(
            reverse('get_post_product_category'),
            data=json.dumps(self.valid_payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_category(self):
        response = client.post(
            reverse('get_post_product_category'),
            data=json.dumps(self.invalid_payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleCategoryTest(TestCase):
    """ Teste module for updating an existing category record """

    def setUp(self):
        self.cat1 = ProductCategory.objects.create(
            id=uuid.uuid4(),
            name="Cat 1",
            description="Cat 1 Desc"
        )
        self.cat2 = ProductCategory.objects.create(
            id=uuid.uuid4(),
            name="Cat 2",
            description="Cat 2 Desc"
        )
        self.valid_payload = {
            'id': str(uuid.uuid4()),
            'name': 'Test Category 1',
            'description': 'Test Category 1 Desc'
        }
        self.invalid_payload = {
            'id': str(uuid.uuid4()),
            'name': '',
            'description': 'Test Category 1 Desc'
        }

    def test_valid_update_category(self):

        response = client.put(
            reverse('get_delete_update_product_category',
                    kwargs={'pk': self.cat1.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_category(self):
        response = client.put(
            reverse('get_delete_update_product_category',
                    kwargs={'pk': self.cat1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleCategory(TestCase):
    """ Test module for deleting an existing category """

    def setUp(self):
        self.cat1 = ProductCategory.objects.create(
            id=uuid.uuid4(),
            name="Cat 1",
            description="Cat 1 Desc"
        )
        self.cat2 = ProductCategory.objects.create(
            id=uuid.uuid4(),
            name="Cat 2",
            description="Cat 2 Desc"
        )

    def test_valid_delete_category(self):
        response = client.delete(
            reverse('get_delete_update_product_category',
                    kwargs={'pk': self.cat1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_category(self):
        response = client.delete(
            reverse('get_delete_update_product_category',
                    kwargs={'pk': uuid.uuid4()})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
