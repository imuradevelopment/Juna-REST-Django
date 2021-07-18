from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import userProfile, User

class userProfileInnerUserSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ('user_id', 'username')

class userProfileListSerializer(serializers.ModelSerializer):
    user = userProfileInnerUserSerializer()
    class Meta:
        model = userProfile
        fields = '__all__'

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        user.username = user_data.get('username', user.username)
        user.save()
        return instance