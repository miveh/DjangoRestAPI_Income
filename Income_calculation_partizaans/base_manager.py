from django.db import models
from rest_framework import status
from rest_framework.exceptions import APIException


class BaseManager(models.Manager):
    def get_or_raise(self, *args, **kwargs):
        queryset = super().get_queryset()
        try:
            return queryset.get(*args, **kwargs)
        except queryset.model.DoesNotExist:
            raise APIException(detail=f'{queryset.model} Does Not Exist', code=status.HTTP_404_NOT_FOUND)

