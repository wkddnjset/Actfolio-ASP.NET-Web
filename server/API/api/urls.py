from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^list/$', ActorView.as_view(), name='actor-list'),
]