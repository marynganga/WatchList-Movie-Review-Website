import unittest
from app.models import Review,User
from app import db

class ReviewTest(unittest.TestCase):
	'''
    Test Class to test the behaviour of the Movie class
    '''

	def setUp(self):
		'''
		Set up method that will run before every Test
		'''
		self.user_James = User(username='James',password='potato',email='james@ms.com')
		self.new_review = Review(movie_id=1234,movie_title='Great Movie',image_path='https://developers.themoviedb.org/3/getting-started/images/khsjha27hbs',movie_review='Would watch it again!',user=self.user_James)

	def tearDown(self):
		Review.query.delete()
		User.query.delete()

	def test_check_instance_variables(self):
		# self.assertTrue(isinstance(self.new_review,Review))
		self.assertEquals(self.new_review.movie_id,1234)
		self.assertEquals(self.new_review.movie_title,'Great Movie')
		self.assertEquals(self.new_review.image_path,'https://developers.themoviedb.org/3/getting-started/images/khsjha27hbs')
		self.assertEquals(self.new_review.movie_review,'Would watch it again!')
		self.assertEquals(self.new_review.user,self.user_James)

	def test_save_review(self):
		self.new_review.save_review()
		self.assertTrue(len(Review.query.all())>0)

	def test_get_review_by_id(self):
		self.new_review.save_review()
		got_reviews = Review.get_reviews(1234)
		self.assertTrue(len(got_reviews)==1)