from rest_framework import status
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException


class WeeklySalaryaClculationError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = _('خطا در محاسبه ی حقوق هفتگی.')


