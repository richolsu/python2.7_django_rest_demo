import django_filters

from quickstart.models import Account


class AccountFilter(django_filters.FilterSet):
    min_age = django_filters.NumberFilter(name="age", lookup_expr='gte')
    max_age = django_filters.NumberFilter(name="age", lookup_expr='lte')

    class Meta:
        model = Account
        fields = ['name', 'min_age', 'max_age']
