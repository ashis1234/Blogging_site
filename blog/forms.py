from django import forms
from django.core import validators
from .models import Post,Category


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag','author','category','body','header_image')

		widgets  = {
			'title': forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Enter title of the blog'}),
			'title_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
			'author' : forms.TextInput(attrs={'class' : 'form-control','id':'elder','value':'','type':'hidden'}),
			# 'author' : forms.Select(attrs={'class' : 'form-control'}),
			'category' : forms.Select(choices = list(Category.objects.all().values_list('name','name')), attrs={'class' : 'form-control'}),
			'body' : forms.Textarea(attrs={'class' : 'form-control','cols': 80, 'rows': 20})
		}

		
class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag','author','category','body','header_image')

		widgets  = {
			'title': forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Enter title of the blog'}),
			'title_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
			# 'author' : forms.Select(attrs={'class' : 'form-control'}),
			'category' : forms.Select(choices = list(Category.objects.all().values_list('name','name')), attrs={'class' : 'form-control'}),
			'body' : forms.Textarea(attrs={'class' : 'form-control','cols': 80, 'rows': 20})
		}
