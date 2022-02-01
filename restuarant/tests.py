from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restuarant.models import Restuarant
from rest_framework.test import RequestsClient

__all__ = ('RestuarantViewTestCase', )


class RestuarantViewTestCase(APITestCase):
	def setUp(self) -> None:
		self.host = "http://127.0.0.1:8000"
		self.base_url = f"{self.host}{reverse('restuarant-list')}"
		self.client = RequestsClient()

	def test_get_list(self):
		data = [
			{'name': 'ResOne', 'address': 'ResOne Address', 'type': 'asian'},
			{'name': 'Res2', 'address': 'ResTwo Address', 'type': 'french'},
			{'name': 'Res3', 'address': 'ResThree Address', 'type': 'free'}
		]
		
		for entry in data:
			Restuarant.objects.create(
				name=entry['name'],
				address=entry['address'],
				type=entry['type']
			)
		response = self.client.get(self.base_url)
		response_data = response.json()
		self.assertEqual(len(response_data), Restuarant.objects.count())

	def test_create(self):
		url = self.base_url
		data = {'name': 'Pualo', 'type': 'free', 'address': 'test address'}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Restuarant.objects.count(), 1)
		self.assertEqual(Restuarant.objects.get().name, 'Pualo')

	def test_filter_by_name(self):
		data = {'name': 'testName', 'address': 'test address', 'type': 'free'}
		res = Restuarant.objects.create(
			name=data['name'],
			address=data['address'],
			type=data['type']
		)
		response = self.client.get(f'{self.base_url}?name=testName')
		result = response.json()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(result), 1)
		self.assertEqual(result[0], {**data, 'id': res.id})

		response = self.client.get(f'{self.base_url}?name=other')
		self.assertEqual(len(response.json()), 0)

