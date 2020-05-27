from django.conf import settings
from rest_framework import serializers

from medical.address.models import Address



class AddressSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    class Meta:
        model = Address
        exclude = ('created_at', 'updated_at')

    def get_images(self, obj):
        """

        :param obj: Address模型类
        :return: 返回图片地址
        """
        queryset = obj.images.all()
        image_list = []
        for q in queryset:
            image_list.append(settings.ALIYUN_PREFIX + str(q.img))

        return image_list
