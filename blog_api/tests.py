from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTests(APITestCase):

    def test_view_post(self):
        url = reverse('blog_api:post-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        self.test_category = Category.objects.create(name='testcategory')
        self.test_user_1 = User.objects.create(username='testuser', password='123456789', is_superuser=True)
        self.client.login(username=self.test_user_1.username,
                          password='123456789')
        self.client.force_authenticate(user=self.test_user_1)
        data = {'title': 'new',
                'author': 1,
                'excerpt': 'new',
                'content': 'new'}
        url = reverse('blog_api:post-list')
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
