from django.db import models
from datetime import datetime
from authors.models import Author

class Article(models.Model):
	author_name = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
	title = models.CharField(max_length=200)
	created_at = models.DateTimeField() 
	tag = models.CharField(max_length=200, default='')
	promo = models.CharField(max_length=200)
	pitch = models.TextField()
	disclosure = models.TextField()
	text = models.TextField()
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
	created_at = models.DateTimeField() 

