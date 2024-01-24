from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .filters import AdvertisementFilter
from .permissions import IsOwner
from .serializers import AdvertisementSerializer
from .models import Advertisement

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['status']
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwner()]
        return []
