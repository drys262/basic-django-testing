import uuid
from django.db import models


class ProductCategory(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sale_price = models.FloatField(default=0, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def is_product_in_sale(self):
        return self.sale_price < 50
