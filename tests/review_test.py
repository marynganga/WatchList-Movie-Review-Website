import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
	'''
    Test Class to test the behaviour of the Movie class
    '''

	def setUp(self):
		'''
		Set up method that will run before every Test
		'''
		self.new_review = Movie(1234,'Great Movie','https://developers.themoviedb.org/3/getting-started/images/khsjha27hbs','Would watch it again!')


	def test_instance(self):
		self.assertTrue(isinstance(self.new_review,Review))

