from .views import ExampleModelView
from django.conf.urls import url

urlpatterns = [
    url(r'^list/$', ExampleModelView.as_view(), name='example-list'),
]