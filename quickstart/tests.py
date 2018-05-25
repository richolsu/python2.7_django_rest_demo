from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

import quickstart
from .models import *


class AccountTests(APITestCase):
    count_before = 0
    test_account = False

    def setUp(self):
        self.test_account = Account.objects.create(name='name 1', age=20)
        Account.objects.create(name='name 2', age=21)
        Account.objects.create(name='name 3', age=22)
        Account.objects.create(name='name 4', age=23)
        Account.objects.create(name='name 5', age=24)
        Account.objects.create(name='name 6', age=25)
        Account.objects.create(name='name 7', age=26)
        Account.objects.create(name='name 8', age=27)
        Account.objects.create(name='name 9', age=28)
        Account.objects.create(name='name 10', age=29)
        Account.objects.create(name='name 11', age=30)
        Account.objects.create(name='name 12', age=31)
        Account.objects.create(name='name 13', age=32)
        Account.objects.create(name='name 14', age=33)
        Account.objects.create(name='name 15', age=34)
        Account.objects.create(name='name 16', age=35)
        Account.objects.create(name='name 17', age=36)
        Account.objects.create(name='name 18', age=37)
        Account.objects.create(name='name 19', age=38)
        Account.objects.create(name='name 20', age=39)
        Account.objects.create(name='name 21', age=40)
        Account.objects.create(name='name 22', age=41)
        Account.objects.create(name='name 23', age=42)
        Account.objects.create(name='name 24', age=43)
        Account.objects.create(name='name 25', age=44)
        Account.objects.create(name='name 26', age=45)
        Account.objects.create(name='name 27', age=46)
        Account.objects.create(name='name 28', age=47)
        Account.objects.create(name='name 29', age=48)

        self.count_before = Account.objects.count()

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        data = {'name': 'new name', 'age': 53}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), self.count_before + 1)

    def test_get_account(self):
        """
        Ensure we can create a new account object.
        """

        response = self.client.get('/accounts/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), self.count_before)

    def test_delete_account(self):
        """
        Ensure we can create a new account object.
        """
        id_before = str(self.test_account.id)

        response = self.client.delete('/accounts/' + id_before + '/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_account(self):
        """
        Ensure we can create a new account object.
        """

        new_name = 'new_name'
        new_age = '5'
        data = {'name': new_name, 'age': new_age}

        id_before = str(self.test_account.id)

        response = self.client.put('/accounts/' + str(id_before) + '/', data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Account.objects.count(), self.count_before)
        self.assertEqual(Account.objects.get(id=id_before).name, new_name)

    def test_filter(self):
        """
        Ensure we can create a new account object.
        """
        response = self.client.get('/accounts/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), self.count_before)
