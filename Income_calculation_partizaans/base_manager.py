from django.db import models
from .exceptions import *


class BaseManager(models.Manager):
    def get_or_raise(self, *args, **kwargs):
        queryset = super().get_queryset()
        try:
            return queryset.get(*args, **kwargs)
        except queryset.model.DoesNotExist:
            raise eval(queryset.model._meta.object_name + 'DoesNotExistException')
