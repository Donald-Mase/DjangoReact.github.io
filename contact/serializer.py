from django.conf import settings

from rest_framework import serializers

from .models import contact


class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = ['Name','Email','Subject','Message']

    def validate_description(self, value):
        if len(value) > 300:
            raise serializers.ValidationError("This is too long")
        return value