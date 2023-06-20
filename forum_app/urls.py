from django.urls import path
from . import views

app_name = "forum_app"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("create-post/", views.create_post, name="create_post"),
    path("category/<int:category_id>/", views.post_list_by_category, name="post_list_by_category"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
]
