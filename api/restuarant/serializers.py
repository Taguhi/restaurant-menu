from rest_framework import serializers

from restuarant.models import Restuarant


class RestuarantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restuarant
        fields = ('id', 'name', 'address', 'type')
