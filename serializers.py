from rest_framework import serializers
from .models import FavoriteQuote

class Favouritequoteserializer(serializers.ModelSerializer):
    class Meta:
        model=FavoriteQuote
        fields='__all__'