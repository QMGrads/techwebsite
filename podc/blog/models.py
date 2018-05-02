from django.db import models
from datetime import datetime    

class Article(models.Model):
	pub_date = models.DateTimeField(default=datetime.now, blank=True)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	article_title = models.CharField(max_length=10000)
	
class Users(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)