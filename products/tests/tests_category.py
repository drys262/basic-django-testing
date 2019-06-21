import uuid


from django.test import TestCase
from ..models import Product, ProductCategory


class ProductCategoryTest(TestCase):
    """ Test module for Product Category model """

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

    def test_category_name(self):
        category_one = ProductCategory.objects.get(name="Test Category 1")
        category_two = ProductCategory.objects.get(name="Test Category 2")

        self.assertEqual(category_one.get_name(), "Test Category 1")
        self.assertEqual(category_two.get_name(), "Test Category 2")
