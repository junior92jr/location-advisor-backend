from rest_framework.routers import DefaultRouter

from .views import RecomendationViewSet


app_name = "recommendations"

router = DefaultRouter()

router.register('', RecomendationViewSet, basename='recomendations_app_url')

urlpatterns = []

urlpatterns += router.urls
