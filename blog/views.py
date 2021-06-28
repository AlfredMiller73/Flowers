from django.shortcuts import render, redirect
from blog.models import Blog, Comment
from blog.forms import CommentForm, BlogForm
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def blog(request):
    """Renders the blog page."""
    last = Blog.objects.order_by('-posted')[:3]
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all() 
    return render(
        request,
        'blog/blog.html',
        {
        'title':'Блог',
        'last': last,
        'posts': posts,
        'year':datetime.now().year,
        }

)

def blogpost(request, id):
    last = Blog.objects.order_by('-posted')[:3]
    post_id = Blog.objects.get(id=id) 
    comments = Comment.objects.filter(post=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user 
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=id) 
            comment_f.save() 
            return redirect('blog:blogpost', id=id) 
    else:
        form = CommentForm() 
    return render(
        request,
        'blog/blogpost.html',
        {
        	'last': last,
            'post_id': post_id, 
            'comments': comments, 
            'form': form, 
            'year':datetime.now().year,
        }
)
