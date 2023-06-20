from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("create-post/", views.create_post, name="create_post"),
    path("", views.post_list, name="post_list"),
]
