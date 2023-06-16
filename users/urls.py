from django.urls import path
from . import views


urlpatterns = [
    path("LoginUser", views.LoginUser, name="login"),
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/create/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
]
