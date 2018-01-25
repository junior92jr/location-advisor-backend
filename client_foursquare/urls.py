# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from client_foursquare import views

app_name = "client_foursquare"

urlpatterns = [
    url(r'^recomendations/$',
        views.RecomendationViewSet.as_view({'get': 'list'})),
]
