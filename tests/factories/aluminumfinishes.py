import factory

from apps.aluminumfinishes.models import AluminumFinishes

class AluminumFinishesFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = AluminumFinishes

    name = "Pulido"
    price = 50700