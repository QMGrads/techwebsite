from django.db import models

class Article(models.Model):
	pub_date = models.DateTimeField('date published')
	Title = models.CharField(max_length=200)
	Author = models.CharField(max_length=100)
	Article = models.CharField(max_length=10000)