from django.shortcuts import render
from articles.models import Article
from django.db.models import Q

def index(request):
	# Get the first article with the tag 10-promise
	firstPromiseArticle = Article.objects.filter(tag = '10-promise').order_by('pk')[:1]

	# Get the id associated with the 10-promise article
	firstPromiseArticleID = Article.objects.filter(tag = '10-promise').order_by('pk')[:1].values('id')
	
	# Retreive the top three articles where the article id is not equal to the article with the 10-promise tag
	# so as not to display the same article twice.
	articleData = Article.objects.filter(~Q(pk=firstPromiseArticleID))[:3]
	
	context = {
		'articleData' : articleData,
		'firstPromiseArticle' : firstPromiseArticle
	}

	return render(request, 'pages/index.html', context)
