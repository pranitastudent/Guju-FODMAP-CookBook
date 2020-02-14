from app import app
import unittest
from flask import Flask, session, url_for

# Check for recipe in database test

class FlaskTestCase(unittest.TestCase):
    """ Test to check recipe description in database (Undhiyu)  """
    def test_task(self):
        # Test a particular recipe description
        tester = app.test_client(self)
        response = tester.get('/task/{}'.format("5e33ff3c1c9d440000bcfe4d"), content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Take 1 cup gram flour" in response.data)
    
    """ Test to check recipe name in db"""    
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Undhiyu" in response.data)
        
# Search Test function

    def test_findtask(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Gluten" in response.data)
        
# Filters - Course and allergens

    def test_filtercourses(self):
        tester = app.test_client(self)
        response = tester.post('/filtercourses', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Main")
        
    def test_filterallergens(self):
        tester = app.test_client(self)
        response = tester.post('/filterallergens', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Nuts")
            
        
                
                
        
            



