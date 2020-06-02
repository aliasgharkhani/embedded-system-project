# serializers.py
from rest_framework import serializers

from .models import ModuleLog


class ModuleLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModuleLog
        fields = ('temperature', 'humidity', 'module_id', 'date')
        extra_kwargs = {'date': {'read_only': True, 'required': False}}
