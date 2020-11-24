from .models import ChartData, chartModel, profileModel
from rest_framework import serializers

class ChartDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChartData
        fields = '__all__'

class ChartSerializers(serializers.ModelSerializer):
    class Meta:
        model = chartModel
        fields = '__all__'

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = profileModel
        fields = '__all__'