from rest_framework import mixins, viewsets

from medical.medicine.serializers import CategorySerializer, MedicineSerializer
from medical.medicine.models import Category, Medicine


class MedicineCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """所有药品和类目的api接口"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class MedicineViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """药品详情接口"""
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
