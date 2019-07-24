from django import forms
from . models import Comments

class CommentForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'cols':100, 'style':'resize:none;'}), label='')
	class Meta:
		model = Comments
		fields = ['comment']
