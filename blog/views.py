from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from django.urls import reverse_lazy,reverse
from .forms import PostForm,EditForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q 
# def home(request):
# 	return render(request,'home.html')

# class Homeview(ListView):
# 	model = Post
# 	template_name = 'home.html'
# 	ordering = ['-post_date']
# 	context_object_name = 'users'  
# 	paginate_by = 5




def SearchView(query=None):
	queryset = []
	queries = query.split(" ") 
	for q in queries:
		posts = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q) | Q(category__icontains=q))
         
		for post in posts:
			queryset.append(post)
	# print(queryset)
	return list(set(queryset))	


BLOG_POSTS_PER_PAGE = 3

def Homeview(request, *args, **kwargs):
	
	context = {}

	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

	blog_posts = sorted(SearchView(query), key=attrgetter('post_date'), reverse=True)
	
	cat_menu = Category.objects.all()
	context['cat_menu'] = cat_menu
		
	# Pagination
	page = request.GET.get('page', 1)
	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
	try:
		blog_posts = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

	context['blog_posts'] = blog_posts

	return render(request, "home1.html", context)






# class SearchView(ListView):
# 	model = Post
# 	template_name = 'search.html'
# 	ordering = ['-post_date']
# 	context_object_name = 'users'  
# 	paginate_by = 5
# 	def get_queryset(self):
# 		query = self.request.GET.get('search_id')
# 		if query:
# 			object_list = Post.objects.filter(Q(title__icontains=query) | Q(category__icontains=query))
# 		return object_list





# class AddCommentView(CreateView):
# 	model = Comment
# 	ordering = ['-date_added']
# 	template_name = 'add_comments.html'
# 	form_class = CommentForm
# 	def form_valid(self,form):
# 		form.instance.post_id = self.kwargs['pk']
# 		form.instance.name = 'Ashis'
# 		return super().form_valid(form)
	

def LikeView(request,pk):
	post = get_object_or_404(Post,id=request.POST.get('post_id'))
	if post.dislikes.filter(id = request.user.id).exists():
		post.dislikes.remove(request.user)	
	post.likes.add(request.user)
	return HttpResponseRedirect(reverse('article',args=[str(pk)]))

def DisLikeView(request,pk):
	post = get_object_or_404(Post,id=request.POST.get('post_id1'))
	if post.likes.filter(id = request.user.id).exists():
		post.likes.remove(request.user)
	post.dislikes.add(request.user)
	return HttpResponseRedirect(reverse('article',args=[str(pk)]))


def category_view(request,cats):
	category_post = Post.objects.filter(category = cats.replace('-',''))
	return render(request,'category.html',{'cats' : cats.title(),'category_post' : category_post})



	
class Articledetails(DetailView):
	model = Post
	template_name = 'detail.html'
	def get_context_data(self,*args,**kwargs):
		cat_menu = Category.objects.all()
		context = super(Articledetails,self).get_context_data(*args,**kwargs)
		context['cat_menu'] = cat_menu
		post = get_object_or_404(Post,id=self.kwargs['pk'])
		liked = False
		if post.likes.filter(id=self.request.user.id).exists():
			liked = True
		disliked = False
		if post.dislikes.filter(id=self.request.user.id).exists():
			disliked = True
		context['total_likes'] = post.total_likes()
		context['liked'] = liked
		context['disliked'] = disliked
		return context



class AddPost(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'addpost.html'
	success_url = reverse_lazy('home')

class UpdatePost(UpdateView):
	model=Post
	form_class = EditForm
	template_name = 'update_post.html'
	success_url = reverse_lazy('home')

class DeletePost(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

class AddCategory(CreateView):
	model = Category
	template_name = 'addcategory.html'
	fields = '__all__'