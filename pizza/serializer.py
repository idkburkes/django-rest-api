from rest_framework import serializers
from .models import Pizza

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'description', 'created_at', 'updated_at')
        model = Pizza