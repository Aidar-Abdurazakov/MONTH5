from django.test import TestCase
from django.urls import reverse

from .models import Category, Product, Review


class ShopApiTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(
            title='Laptop',
            description='Gaming laptop',
            price='999.99',
            category=self.category,
        )
        self.review = Review.objects.create(text='Great device', product=self.product)

    def test_category_list_endpoint(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_category_detail_endpoint(self):
        response = self.client.get(reverse('category-detail', kwargs={'id': self.category.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Electronics')

    def test_product_list_endpoint(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_product_detail_endpoint(self):
        response = self.client.get(reverse('product-detail', kwargs={'id': self.product.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], 'Laptop')

    def test_review_list_endpoint(self):
        response = self.client.get(reverse('review-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_review_detail_endpoint(self):
        response = self.client.get(reverse('review-detail', kwargs={'id': self.review.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['text'], 'Great device')
