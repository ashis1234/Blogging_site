from django.urls import path
from .views import UserRegistrationView,UserEditView,UserPassword_changeView,ProfileView,EditProfileView,CreateProfileView,UserPassword_change_without_old_View,Non_created_user_profile_view
urlpatterns = [
    path('register/',UserRegistrationView,name = 'register'),
    path('edit_profile/',UserEditView.as_view(),name = 'edit_profile'),
    path('password/',UserPassword_changeView.as_view(),name = 'password_change'),
    path('<int:pk>/',ProfileView,name ='user_profile'),
    path('<int:pk>/edit_profile_page/',EditProfileView.as_view(),name ='edit_profile_page'),
    path('create_profile/',CreateProfileView.as_view(),name = 'create_profile'),
    path('without_password/',UserPassword_change_without_old_View.as_view(),name = 'without_password'),
    path('<slug:name>/',Non_created_user_profile_view,name ='user_profile1'),
]
