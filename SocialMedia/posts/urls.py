from django.urls import path
from . import views

urlpatterns = [
    path("create-post/", views.create_post, name="create_post"),
    path("posts/", views.all_posts, name="all_posts"),
    path("like/<int:post_id>/", views.like_post, name="like_post"),
    path("comment/<int:post_id>/", views.add_comment, name="add_comment"),
    path("delete-post/<int:post_id>/", views.delete_post, name="delete_post"),
    path("delete-comment/<int:comment_id>/", views.delete_comment, name="delete_comment"),
]