from django.conf.urls import url
from . import rest

urlpatterns = [
    url(r'^generate$', rest.generate),
    url(r'^user$', rest.user),
]