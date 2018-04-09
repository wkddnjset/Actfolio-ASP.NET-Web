from rest_framework import serializers
from ..models import ExampleModel

class ExampleModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = [
            'id',
            'text',
            'img'
        ]