from django.shortcuts import render
from articles.models import Article

def index(request):
	articleData = Article.objects.all()[:3]
	firstPromiseArticle = Article.objects.filter(tag = '10-promise')[:1]
	
	context = {
		'articleData' : articleData,
		'firstPromiseArticle' : firstPromiseArticle
	}

	return render(request, 'pages/index.html', context)
