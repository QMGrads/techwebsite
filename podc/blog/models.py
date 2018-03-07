from django.db import models

class Article(models.Model):
	pub_date = models.DateTimeField('date published')
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	article_title = models.CharField(max_length=10000)