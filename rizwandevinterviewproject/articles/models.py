from django.db import models
from datetime import datetime
from authors.models import Author

class Article(models.Model):
	author_name = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
	title = models.CharField(max_length=200)
	created_at = models.DateTimeField() 
	tag = models.CharField(max_length=200, default='')
	text = models.TextField() 
	photo_main = models.ImageField(upload_to='photos', blank=True)
	photo_1 = models.ImageField(upload_to='photos', blank=True)
	photo_2 = models.ImageField(upload_to='photos', blank=True)
	photo_3 = models.ImageField(upload_to='photos', blank=True)
	photo_4 = models.ImageField(upload_to='photos', blank=True)
	def __str__(self):
		return self.title


class StockQuotes(models.Model):
	CompanyName = models.CharField(max_length=200)
	Symbol = models.CharField(max_length=10)
	CurrentPrice = models.DecimalField(max_digits=10, decimal_places=2)
	Change = models.DecimalField(max_digits=10, decimal_places=2)
	PercentChange = models.DecimalField(max_digits=10, decimal_places=2)
	def __str__(self):
		return self.CompanyName


class Comments(models.Model):
	article_id = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
	comment = models.TextField()

