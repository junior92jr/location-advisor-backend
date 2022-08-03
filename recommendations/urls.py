from django.urls import include, path


from recommendations import views

app_name = "recommendations"

urlpatterns = [
    path('recomendations/',
        views.RecomendationViewSet.as_view({'get': 'list'})),
]
