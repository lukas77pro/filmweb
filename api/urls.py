from django.conf.urls import url
from . import rest, gendata

urlpatterns = [
    url(r'^generate$', gendata.generate),
    url(r'^countries$', rest.countries),
    url(r'^professions', rest.professions),
    url(r'^genres', rest.genres),
    url(r'^user$', rest.user),
    url(r'^film$', rest.film),
    url(r'^person$', rest.person),
]