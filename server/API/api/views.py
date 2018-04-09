from rest_framework import generics
from ..models import ExampleModel
from .serializers import ExampleModelSerializers

class ExampleModelView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ExampleModelSerializers
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return ExampleModel.objects.all()