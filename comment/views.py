from django.shortcuts import get_object_or_404, redirect
from .models import Comment
from django.http import HttpResponseForbidden
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Check if the request user is the owner of the comment or has permission to delete it
    if comment.user == request.user:
        # Delete the comment
        comment.delete()
        # Redirect to a success page or any other page as per your requirement
        return redirect('post-details', post_id=comment.post.id)
    else:
        # If the request user is not the owner of the comment, return a forbidden response
        return HttpResponseForbidden("You don't have permission to delete this comment.")
