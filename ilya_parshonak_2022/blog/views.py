from django.shortcuts import render
from .models import Post, Comment
# Create your views here.

def blog_index(request):
    post = Post.objects.all().order.by('-created_on')
    context = {
        'posts': post
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        'posts': post,
        "coments": comments,
    }
    return render(request, 'blog_detail.html', context)

