from django.shortcuts import render
from articles.models import Article
from django.db.models import Q

def index(request):
	firstPromiseArticle = Article.objects.filter(tag = '10-promise').order_by('pk')[:1]
	firstPromiseArticleID = Article.objects.filter(tag = '10-promise').order_by('pk')[:1].values('id')
	articleData = Article.objects.filter(~Q(pk=firstPromiseArticleID))[:3]
	
	context = {
		'articleData' : articleData,
		'firstPromiseArticle' : firstPromiseArticle
	}

	return render(request, 'pages/index.html', context)
