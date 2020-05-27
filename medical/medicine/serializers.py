
from rest_framework import serializers

from medical.medicine.models import Category, Medicine


class MedicineBriefSerializer(serializers.ModelSerializer):
    """药品简要内容序列化"""
    class Meta:
        model = Medicine
        fields = ('id', 'name', 'image', "normal_price", "promotion_price", "sn",
                  "stock", "sold_num", 'symptom')



class CategorySerializer(serializers.ModelSerializer):
    """类目和蛋糕序列化"""
    medicine_set = MedicineBriefSerializer(many=True) # 类目的所有商品
    class Meta:
        model = Category
        fields = ("id", "name", "medicine_set")


class MedicineSerializer(serializers.ModelSerializer):
    """蛋糕详情序列化"""
    tags = serializers.SerializerMethodField()
    class Meta:
        model = Medicine
        exclude = ('created_at', 'updated_at')

    def get_tags(self, obj):
        return ",".join([tag.name for tag in obj.tags.all()])
