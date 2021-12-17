from django.urls import path
from .views import *

urlpatterns = [
    path('income/<int:id>/', IncomeAPIView.as_view(), name='income'),
    path('increase/<int:id>/', csrf_exempt(IncreaseAPIView.as_view()), name='increase_income'),
    path('deduction/<int:id>/', csrf_exempt(DeductionIncomeAPIView.as_view()), name='deduction_income'),
]
