from django.test import TestCase
from django.urls import reverse
# testing can only be conducted when connected to the local SQLite 3, due to secuirty issues on postgres


class URLTests(TestCase):

   
    def test_defaultpage_url(self):
        # Test the index page loads (e.g., '/')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_url(self):
        # Test the home page URL (e.g., '/')
        response = self.client.get(reverse('home')) 
        self.assertEqual(response.status_code, 200)
    
    def test_alltrips_url(self):
        # Test the all trips page URL (e.g., 'all trips')
        response = self.client.get(reverse('alltrips'))
        self.assertEqual(response.status_code, 200)

    def test_bag_url(self):
        # Test the bag page URL (e.g., URL 'bag')
        response = self.client.get(reverse('view_bag')) 
        self.assertEqual(response.status_code, 200)
    
    def test_checkout_url(self):
        # Test the checkout page URL (e.g., URL 'checkout')
        response = self.client.get(reverse('checkout')) 
        self.assertEqual(response.status_code, 302)

     
    
