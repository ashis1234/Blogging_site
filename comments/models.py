from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from blog.models import Post
from django.conf import settings

class Comment(models.Model):
	user      =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
	# post      =  models.ForeignKey(Post,on_delete = models.CASCADE)
	content_type = models.ForeignKey(ContentType,null=True, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField(null=True)
	content_object = GenericForeignKey('content_type', 'object_id')
	content   =  models.TextField()
	timestamp =  models.DateTimeField(auto_now_add = True)
	
	def __unicode__(self):
		return str(self.user.username)
	def __str__(self):
		return str(self.user.username)
