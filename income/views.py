from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from rest_framework.generics import CreateAPIView

from income.models import Courier
from income.serializers import (
    IncomeSerializer,
    IncreaseIncomeSerializer,
    DeductionIncomeSerializer,
)


class IncomeAPIView(CreateAPIView):
    """
    API for create Income ,this API needs to Authenticate permission but ignore it now.
    """

    serializer_class = IncomeSerializer

    def perform_create(self, serializer):
        serializer.save(courier=Courier.objects.get(id=self.kwargs.get('id')))
        return serializer


class IncreaseAPIView(CreateAPIView):
    """
    API for increase Income ,this API needs to Authenticate permission but ignore it now.
    """

    serializer_class = IncreaseIncomeSerializer

    def perform_create(self, serializer):
        serializer.save(courier=Courier.objects.get(id=self.kwargs.get('id')))
        # return serializer


class DeductionIncomeAPIView(CreateAPIView):
    """
    API for deduction Income ,this API needs to Authenticate permission but ignore it now.
    """

    serializer_class = DeductionIncomeSerializer

    def perform_create(self, serializer):
        serializer.save(courier=Courier.objects.get(id=self.kwargs.get('id')))
        return serializer


