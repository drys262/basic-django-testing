import factory


from products.models import Product, ProductCategory


# factory.Faker._DEFAULT_LOCALE = 'es_ES'


class ProductCategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = ProductCategory

    name = factory.Faker('name')
    description = factory.Faker('text')


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product

    category = factory.SubFactory(ProductCategoryFactory)
    name = factory.Faker('name')
    sale_price = factory.Faker('number')
