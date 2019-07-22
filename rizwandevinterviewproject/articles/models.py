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
