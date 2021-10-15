from rest_framework import serializers
from . models import Table
from django.forms import fields


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = {
            'title', 'description'
        }
