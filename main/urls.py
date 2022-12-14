from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('settings/',views.settings, name='settings'),
    path('upload',views.upload,name='upload'),
    path('profile/<str:pk>',views.profil,name='profile'),
    path('like-post',views.like_post,name='like-post'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout,name='logout'),
]
