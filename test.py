from app import app
import unittest
from flask import Flask, session, url_for

# Check for recipe in database test

class FlaskTestCase(unittest.TestCase):
    
    """ Test Register function"""
    
    def test_register(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Username" in response.data)
        
    """ Test Login function"""
    
    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Password" in response.data) 
        
    """ Test Logout function"""
    
    def test_logout(self):
        tester = app.test_client(self)
        response = tester.get('/logout', content_type='html/text')
        self.assertEqual(response.status_code, 302)
    
     
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

    """ Test to check search function"""    
    def test_findtask(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Gluten" in response.data)
        
# Filters - Course and allergens

    """ Test to check filtering of courses"""    
    def test_filtercourses(self):
        tester = app.test_client(self)
        response = tester.post('/filtercourses', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Main" in response.data)
        
        
    """ Test to filtering of allergens"""        
    def test_filterallergens(self):
        tester = app.test_client(self)
        response = tester.post('/filterallergens', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Nuts")
        
# Add a recipe 
     
    """ Test addition of recipe"""        
    def test_create_task(self):
        tester = app.test_client(self)
        response = tester.post('/create_task', content_type='html/text')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"Recipe Name")  
        
    """ Test editing a recipe"""
    def test_update_task(self):
        tester = app.test_client(self)
        response = tester.post('/create_task', content_type='html/text')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"Cooking Time")           
        
            



