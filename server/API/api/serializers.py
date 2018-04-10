from rest_framework import serializers
from ..models import *

class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = [
            'name',
            'email',
            'phone',
            'img'
        ]