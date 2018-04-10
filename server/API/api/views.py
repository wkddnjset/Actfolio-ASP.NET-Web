from rest_framework import generics
from ..models import *
from .serializers import *

class ActorView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ActorSerializers
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return Actor.objects.all()