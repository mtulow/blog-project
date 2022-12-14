from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/', views.posts, name='posts'),
    path('comments/', views.comments, name='comments'),
]