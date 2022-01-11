from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','firstName','lastName','phoneNumber','email','category')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.email = validated_data.get('email',instance.email)
        instance.category = validated_data.get('category',instance.category)
        instance.save()
        return instance
