from django.urls import path
from .views import Homeview,Articledetails,AddPost,UpdatePost,DeletePost,AddCategory,category_view,LikeView,DisLikeView,SearchView

urlpatterns = [
    path('', Homeview,name='home'),
    path('article/<int:pk>/',Articledetails.as_view(),name='article'),
    path('like/<int:pk>/',LikeView,name='like_post'),
    path('dislike/<int:pk>/',DisLikeView,name='dislike_post'),
    path('addpost/', AddPost.as_view(),name='addpost'),
    path('addcategory/', AddCategory.as_view(),name='addcategory'),
    path('article/edit/<int:pk>/',UpdatePost.as_view(),name='update_post'),
    path('article/<int:pk>/remove/',DeletePost.as_view(),name='delete_post'),
    path('category/<str:cats>/',category_view,name='category'),
    # path('article/<int:pk>/comments/',AddCommentView.as_view(),name = 'add_comments'),
    path('search/', SearchView,name='search'),
]


