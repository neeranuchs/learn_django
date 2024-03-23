from rest_framework import serializers,generics
from . import models

class ItemSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     # Automatically set created_at field
    #     instance = models.Item.objects.create(**validated_data)
    #     print(instance)
    #     return instance
    class Meta:
        model = models.Item
        # fields = ("title", "detail", "is_completed")
        # read_only_fields = ('created_at', 'updated_at', "deleted_at")
        fields = '__all__'
        