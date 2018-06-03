from django.db import models
from datetime import datetime    

class Article(models.Model):
	pub_date = models.DateTimeField(default=datetime.now, blank=True)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	article_title = models.TextField()
	article_image = models.ImageField(upload_to='article_image', blank=True)
	
class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)