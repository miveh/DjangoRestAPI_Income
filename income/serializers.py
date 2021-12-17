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
