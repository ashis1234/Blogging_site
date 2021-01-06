from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
	# email = forms.EmailField()
	# first_name = forms.CharField(max_length = 250)
	# last_name = forms.CharField(max_length = 250)
	class Meta:
		model = User
		fields = ('username','password1')

	def __init__(self,*args,**kwargs):
		super(SignupForm,self).__init__(*args,**kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control' 
		self.fields['password1'].widget.attrs['class'] = 'form-control' 
		# self.fields['password2'].widget.attrs['class'] = 'form-control' 
		# self.fields['first_name'].widget.attrs['class'] = 'form-control' 
		# self.fields['last_name'].widget.attrs['class'] = 'form-control' 
		# self.fields['email'].widget.attrs['class'] = 'form-control' 