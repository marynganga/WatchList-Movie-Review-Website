from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class Movie:
	'''
    Movie class to define Movie Objects
    '''
	def __init__(self,id,title,overview,image,vote_average,vote_count):
		'''
		Args: 
			1. Title - The name of the movie
			2. Overview - A short description on the movie
			3. image- The poster image for the movie
			4. vote_average - Average rating of the movie
			5. vote_count - How many people have rated the movie
			6. id - The movie id
		'''
		self.id =id
		self.title = title
		self.overview = overview
		self.image = "https://image.tmdb.org/t/p/w300{}".format(image)
		self.vote_average = vote_average
		self.vote_count = vote_count

class Review(db.Model):
	'''
	Review class to define Review Objects
	'''
	__tablename__ = 'reviews'
	id = db.Column(db.Integer,primary_key = True)
	movie_id = db.Column(db.Integer)
	movie_title = db.Column(db.String)
	image_path = db.Column(db.String)
	movie_review = db.Column(db.String)
	posted = db.Column(db.DateTime,default=datetime.utcnow)
	user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

	def save_review(self):
		# Review.all_reviews.append(self)
		db.session.add(self)
		db.session.commit()

	# @classmethod
	# def clear_reviews(cls):
	# 	Review.all_reviews.clear()

	@classmethod
	def get_reviews(cls,id):
		# response = []

		# for review in cls.all_reviews:
		# 	if review.movie_id == id:
		# 		response.append(review)

		# return response
		reviews = Review.query.filter_by(movie_id=id).all()
		return reviews 

class User(UserMixin,db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(255))
	role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
	email = db.Column(db.String(255),unique=True,index=True)
	bio = db.Column(db.String(255))
	profile_pic_path = db.Column(db.String())
	pass_secure = db.Column(db.String(255))
	reviews = db.relationship('Review',backref='user',lazy='dynamic')

	@property
	def password(self):
		raise AttributeError('You cannot read the password attribute.')

	@password.setter
	def password(self, password):
		self.pass_secure = generate_password_hash(password)

	def verify_password(self,password):
		return check_password_hash(self.pass_secure,password)

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

		
	def __repr__(self):
		return f'User {self.username}'


class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(255))
	users = db.relationship('User',backref = 'role', lazy = 'dynamic')
	def __repr__(self):
		return f'User {self.name}'
