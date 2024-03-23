from rest_framework import serializers,generics
from . import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Personnel
        fields = '__all__'