from django.conf.urls import url
from . import rest, gendata

urlpatterns = [
    url(r'^generate$', gendata.generate),
    url(r'^user$', rest.user),
    url(r'^film$', rest.film),
]