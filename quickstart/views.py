
from rest_framework import generics, viewsets, filters

from quickstart.filters import AccountFilter
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_class = AccountFilter


class AccountListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name', 'age')
    ordering = ('name',)




