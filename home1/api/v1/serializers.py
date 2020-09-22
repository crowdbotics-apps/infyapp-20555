from rest_framework import serializers
from home1.models import US


class USSerializer(serializers.ModelSerializer):
    class Meta:
        model = US
        fields = "__all__"
