from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),

]
