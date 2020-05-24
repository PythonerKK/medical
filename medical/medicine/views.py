from rest_framework import mixins, viewsets

from medical.medicine.serializers import CategorySerializer
from medical.medicine.models import Category


class MedicineCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """所有药品和类目的api接口"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
