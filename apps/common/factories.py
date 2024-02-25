import factory
from .models import Data


class DataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Data

    name = factory.Faker('name')
    description = factory.Faker('text')
    data_json = factory.Faker('json')
