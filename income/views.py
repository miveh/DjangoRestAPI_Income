from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from rest_framework.generics import CreateAPIView, ListAPIView

from income.models import Courier, WeeklyIncome
from income.serializers import (
    IncomeSerializer,
    IncreaseIncomeSerializer,
    DeductionIncomeSerializer, WeeklyIncomeSerializer,
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


class WeeklyIncomeListAPIView(ListAPIView):
    """
    API for display list of weekly income
    """
    serializer_class = WeeklyIncomeSerializer
    queryset = WeeklyIncome.objects.all()
    # def get_queryset(self):
    #     from_date, to_date = self.request.query_params.get('from_date'), self.request.query_params.get('to_date')



