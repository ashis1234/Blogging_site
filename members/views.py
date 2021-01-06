from django.shortcuts import render,get_object_or_404
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm,SetPasswordForm
from django.urls import reverse_lazy,reverse
from .forms import SignupForm
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView
from blog.models import Profile,Post
from django.contrib.auth.models import User



class CreateProfileView(generic.CreateView):
	model = Profile
	template_name = 'registration/create_profile_page.html'
	fields = '__all__'
	success_url = reverse_lazy('home')
	def form_valid(self,form):
		form.instance.user = self.request.user
		return super().form_valid(form)

def UserRegistrationView(request):
	if request.method=='POST':
		fm = SignupForm(request.POST)
		if fm.is_valid():
			fm.save()
	else:
		fm = SignupForm()
	return render(request,'registration/register.html',{'form' : fm})




class EditProfileView(generic.UpdateView):
	model = Profile
	template_name = 'registration/edit_profile_page.html'
	fields = ['bio','pic','website_url','facebook_url','instagram_url','linkdin_url','twiter_url','github_url']
	success_url = reverse_lazy('home')






# class ProfileView(generic.DetailView):
# 	model = Profile
# 	template_name = 'registration/profile.html'
# 	def get_context_data(self,*args,**kwargs):
# 		# print(self.kwargs['pk'])
# 		context = super(ProfileView,self).get_context_data(*args,**kwargs)
# 		# profile_user = get_object_or_404(Profile,id=self.kwargs[pk])
# 		# profile_user = "Anonomoys_user"
		
# 		if Profile.objects.filter(id=self.kwargs['pk']).exists():
# 			profile = Profile.objects.filter(id=self.kwargs['pk'])
# 			context['profile_user'] = profile[0]
# 		else:
# 			context['profile_user'] = profile_user
# 		return context


def ProfileView(request,pk):
	context = {}
	if Profile.objects.filter(id=pk).exists():
		profile = Profile.objects.filter(id=pk)
		context['profile_user'] = profile[0]
	return render(request,'registration/profile.html',context)

def Non_created_user_profile_view(request,name):
	context = {}
	context['profile_user'] = name
	return render(request,'registration/profile.html',context)






# class UserRegistrationView(generic.CreateView):
# 	form_class = SignupForm
# 	template_name = 'registration/register.html'
# 	success_url = reverse_lazy('login') 



class UserEditView(generic.UpdateView):
	form_class = UserChangeForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')
	def get_object(self):
		return self.request.user


class UserPassword_changeView(PasswordChangeView):
	form_class = PasswordChangeForm
	template_name = 'registration/password_change.html'
	success_url = reverse_lazy('home') 
	

class UserPassword_change_without_old_View(PasswordChangeView):
	form_class = SetPasswordForm
	template_name = 'registration/without_password_change.html'
	success_url = reverse_lazy('home') 
	

