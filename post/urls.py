from django.urls import path
from post.views import index, NewPost, PostDetail, Tags, like, favourite,delete_post

urlpatterns = [
    path('', index, name='index'),
    path('newpost', NewPost, name='newpost'),
    path('<uuid:post_id>', PostDetail, name='post-details'),
    path('tag/<slug:tag_slug>', Tags, name='tags'),
    path('<uuid:post_id>/like', like, name='like'),
    path('<uuid:post_id>/favourite', favourite, name='favourite'),
     path('post/<uuid:post_id>/delete/', delete_post, name='delete-post'),
]
