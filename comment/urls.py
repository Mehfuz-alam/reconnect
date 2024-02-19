from django.urls import path
from . import views

urlpatterns = [
    
   path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete-comment'),

]
