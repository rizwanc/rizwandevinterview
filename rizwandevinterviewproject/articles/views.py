from django.shortcuts import get_object_or_404, render

from .models import Article

def index(request):
	return render(request, 'articles/article.html')


def article(request, article_id):
	article = get_object_or_404(Article, pk=article_id)

	context = {
		'article': article
	}

	request.encoding = 'UTF-8-SIG'
	return render(request, 'articles/article.html', context)