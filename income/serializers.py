from rest_framework import serializers

from income.models import *


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['amount']


class IncreaseIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncreaseIncome
        fields = ['amount']


class DeductionIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeductionIncome
        fields = ['amount']


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class WeeklyIncomeSerializer(serializers.ModelSerializer):
    courier = serializers.SerializerMethodField()
    class Meta:
        model = WeeklyIncome
        fields = '__all__'

    def get_courier(self, obj):
        return CourierSerializer(Courier.objects.get(weeklyincome=obj)).data


