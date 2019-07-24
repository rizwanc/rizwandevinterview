from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from random import randint
from django.db.models import Q
from datetime import datetime
from .models import Article, StockQuotes, Comments
from .forms import CommentForm

def article(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	stockQuotes = StockQuotes.objects.all()[:3] 
	comments = Comments.objects.filter(article_id_id = article_id)
	articleLinks = Article.objects.filter(~Q(pk=article_id))[:5]

	if request.method == 'POST':
		# A comment was posted
	 	comment_form = CommentForm(data=request.POST)
	 	if comment_form.is_valid():
	 		# create the comment object but dont save yet
	 		new_comment = comment_form.save(commit=False)
	 		# Assign the current article id to the comment 
	 		new_comment.article_id_id = article_id
	 		# Assign the current time for when the comment was made
	 		new_comment.created_at = datetime.now()
	 		# Save the comment to the database
	 		new_comment.save()
	 		# Create new form to clear any old comments
	 		comment_form = CommentForm()
	 		# Redirect to the same page to prevent resubmits on refresh
	 		return HttpResponseRedirect("")
	else:
		comment_form = CommentForm()

	context = {
	'article': article,
	'stockQuotes': stockQuotes,
	'articleLinks': articleLinks,
	'comment_form': comment_form,
	'comments': comments
	}
	
	return render(request, 'articles/article.html', context)
	
	

	

	
	

