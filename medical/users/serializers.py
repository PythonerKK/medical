
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'nickname', 'gender', 'mobile', 'avatar_url', 'address')
