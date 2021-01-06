from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from django.utils import timezone
from ckeditor.fields import RichTextField

class Profile(models.Model):
	user = models.OneToOneField(User,null=True,on_delete=models.CASCADE,related_name = 'profile')
	bio = models.TextField(default="Profile not updated yet")
	pic = models.ImageField(null=True,blank=True,upload_to='images/')
	website_url = models.CharField(null=True,max_length=250)
	linkdin_url = models.CharField(null=True,max_length=250)
	facebook_url = models.CharField(null=True,max_length=250)
	github_url = models.CharField(null=True,max_length=250)
	instagram_url = models.CharField(null=True,max_length=250)
	twiter_url = models.CharField(null=True,max_length=250)
	def __str__(self):
		return str(self.user)
	
		

class Category(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('home')

		

class Post(models.Model):
	title = models.CharField(max_length=250)
	title_tag = models.CharField(max_length=250,default="Ashis Blog")
	header_image = models.ImageField(null=True,blank=True,upload_to='images/')
	author = models.ForeignKey(User,on_delete = models.CASCADE)
	# body = models.TextField()
	body = RichTextField(blank=True,null=True)
	post_date = models.DateField(auto_now_add = True)
	category = models.CharField(max_length=255,default = 'coding')
	likes = models.ManyToManyField(User,related_name = 'blog_posts')
	dislikes = models.ManyToManyField(User,related_name = 'blog_posts1')
	
	def total_likes(self):
		return self.likes.count() - self.dislikes.count()
		
	def __str__(self):
		return self.title + '|' + str(self.author)

	def get_absolute_url(self):
		return reverse('article',args = (str(self.id)))

# class Comment(models.Model):
# 	post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
# 	name = models.CharField(max_length=250)
# 	body = models.TextField()
# 	date_added = models.DateTimeField(auto_now_add=True)
# 	def get_absolute_url(self):
# 		return reverse('article',args = str(self.post_id))