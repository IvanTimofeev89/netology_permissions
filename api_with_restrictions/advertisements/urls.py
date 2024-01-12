
from rest_framework.routers import DefaultRouter

from .views import AdvertisementViewSet

router = DefaultRouter()
router.register('advertisements', AdvertisementViewSet, basename='advertisement')

urlpatterns = router.urls
