from django.shortcuts import render

def index(request):
	return render(request, 'articles/article.html')


def article(request):
	return render(request, 'articles/article.html')