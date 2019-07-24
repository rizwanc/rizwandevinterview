from django.shortcuts import get_object_or_404, render
from random import randint
from .models import Article, StockQuotes, Comments
from .forms import CommentForm

def article(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	stockQuotes = StockQuotes.objects.all()[:3] 
	comments = Comments.objects.filter(article_id_id = article_id)

	if request.method == 'POST':
		# A comment was posted
	 	comment_form = CommentForm(data=request.POST)
	 	if comment_form.is_valid():
	 		new_comment = comment_form.save(commit=False)
	 		new_comment.article_id_id = article_id
	 		new_comment.save()
	else:
		comment_form = CommentForm()

	context = {
	'article': article,
	'stockQuotes': stockQuotes,
	'comment_form': comment_form,
	'comments': comments
	}
	
	#context['comment_form'].fields['article_id'].initial = article_id

	return render(request, 'articles/article.html', context)
	
	

	

	
	

