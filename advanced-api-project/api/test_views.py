from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Define valid and invalid payloads
        self.valid_payload = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': 1  # Ensure author ID exists
        }
        self.invalid_payload = {
            'title': '',
            'publication_year': 2024,
            'author': 1
        }
        
        # Create a sample book
        self.book = Book.objects.create(**self.valid_payload)

    def test_create_book(self):
        response = self.client.post('/api/books/', self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_update_book(self):
        response = self.client.put(f'/api/books/{self.book.id}/', {'title': 'Updated Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book.id).title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        response = self.client.get('/api/books/', {'title': 'New Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books(self):
        response = self.client.get('/api/books/', {'search': 'New Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_ordering_books(self):
        response = self.client.get('/api/books/', {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['results'][0]['title'] == 'New Book')
