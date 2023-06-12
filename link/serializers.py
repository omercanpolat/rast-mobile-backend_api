from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"

    def validate(self, data):
        if data["link_name"] == data["description"]:
            raise serializers.ValidationError({"message":"Link Adı ile Açıklama aynı olamaz!"})
        return data
