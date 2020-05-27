from rest_framework import mixins, viewsets

from medical.address.serializers import AddressSerializer
from medical.address.models import Address


class AddressViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    list:
    返回所有医务室信息

    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
