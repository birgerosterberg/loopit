from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('delete_post/<slug:slug>/',
         views.DeletePostView.as_view(), name='delete_post'),
    path('edit_post/<slug:slug>/',
         views.EditPostView.as_view(), name='edit_post'),

]
