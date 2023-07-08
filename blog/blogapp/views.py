from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogapp/post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blogapp/create_post.html', {'form': form})
