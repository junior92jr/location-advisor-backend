from django.urls import include, path


from client_foursquare import views

app_name = "client_foursquare"

urlpatterns = [
    path('recomendations/',
        views.RecomendationViewSet.as_view({'get': 'list'})),
]
