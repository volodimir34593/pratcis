# app_name/views.py
from django.shortcuts import render
from .models import Author, Post, Comment

def stats_view(request):
   
    author = Author.objects.first()

    
    comment_count = author.posts.count()

    
    long_comment_count = Comment.objects.filter(post__author=author, text__length__gte=5).count()

    context = {
        'author': author,
        'comment_count': comment_count,
        'long_comment_count': long_comment_count,
    }
    return render(request, 'app_name/stats.html', context)