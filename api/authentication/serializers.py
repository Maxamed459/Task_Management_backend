from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer (serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirmation']

    def validate(self, data):
        if data["password"] != data["confirmation"]:
            raise serializers.ValidationError("passwords must match")
        return data
         

    def create(self, validated_data):
        validated_data.pop("confirmation")
        user = User.objects.create_user(
            username = validated_data["username"],
            email = validated_data["email"],
            password = validated_data["password"],
        )
        return user
