from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        data = {'name': 'DabApps', 'age': '3'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'DabApps')

    def test_get_account(self):
        """
        Ensure we can create a new account object.
        """

        Account.objects.create(name='question_text1', age=2)
        Account.objects.create(name='question_text2', age=3)

        response = self.client.get('/accounts/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{"name": "question_text1", "age": "2"}, {"name": "question_text2", "age": "3"}])

    def test_delete_account(self):
        """
        Ensure we can create a new account object.
        """

        account1 = Account.objects.create(name='name1', age=2)
        account2 = Account.objects.create(name='name2', age=3)

        response = self.client.delete('/accounts/' + str(account1.id) + '/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, account2.name)

    def test_update_account(self):
        """
        Ensure we can create a new account object.
        """

        account = Account.objects.create(name='name', age=2)
        new_name = 'new_name'
        new_age = '5'
        data = {'name': new_name, 'age': new_age}
        response = self.client.put('/accounts/' + str(account.id) + '/', data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, new_name)
        self.assertEqual(Account.objects.get().age, new_age)

