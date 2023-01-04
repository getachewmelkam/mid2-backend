from rest_framework import serializers
from .models import teacher


class teacherserializer(serializers.ModelSerializer):
    class Meta:
        model=teacher
        fields='__all__'