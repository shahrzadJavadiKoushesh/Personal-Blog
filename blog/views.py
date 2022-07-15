from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from .forms import NewPostForm


def post_list_view(request):
    posts_list = Post.objects.filter(status='pub')
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    sample_post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': sample_post})


def post_create_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            form = NewPostForm()
    else: # GET request
        form = NewPostForm()
    return render(request, 'blog/post_create.html', context={'form': form})
    # written without model forms :
    # if request.method == 'POST':
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     # django ORM
    #     sample_user = User.objects.all()[0]
    #     Post.objects.create(title=post_title, text=post_text, author=sample_user, status='pub')
    # else:
    #     print("GET request")
    # return render(request, 'blog/post_create.html')