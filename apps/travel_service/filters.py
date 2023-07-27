import django_filters
from .models import *


class SearshFilter(django_filters.FilterSet):
    class Meta:
        model = Search
        fields = '__all__'


class TransferFilter(django_filters.FilterSet):
    class Meta:
        model = Transfer
        fields = '__all__'
