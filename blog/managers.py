from django.db import models
from django.db.models import Q


class PublicPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(scope='PUBLIC')


class StaffPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(scope='PUBLIC') & Q(scope='STAFF'))


class SuperUserPostManager(models.Manager):
    pass
