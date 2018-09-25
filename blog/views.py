from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {"posts": posts})
	
def about(request):
    about = Post.objects.filter(title__contains='About')
    return render(request, 'blog/about.html', {'about':about})