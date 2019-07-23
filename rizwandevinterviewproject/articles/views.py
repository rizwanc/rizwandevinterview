from django.shortcuts import get_object_or_404, render
from random import randint
from .models import Article, StockQuotes

def index(request):
	return render(request, 'articles/article.html')


def article(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	stockQuotes = StockQuotes.objects.all()[:3] 

	context = {
		'article': article,
		'stockQuotes': stockQuotes
	}

	request.encoding = 'UTF-8-SIG'
	return render(request, 'articles/article.html', context)