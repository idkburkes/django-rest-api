from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Pizza

class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_thing = Pizza.objects.create(name='Meat Lover', owner=testuser1,description='Loaded with sausage, pepperoni, and ham.')
        test_thing.save()

    def test_pizza_model(self):
        pizza = Pizza.objects.get(id=1)
        actual_owner = str(pizza.owner)
        actual_name = str(pizza.name)
        actual_description = str(pizza.description)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_name, 'Meat Lover')
        self.assertEqual(actual_description,'Loaded with sausage, pepperoni, and ham.')