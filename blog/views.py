from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post
from django.views import generic
from django.urls import reverse_lazy


# def post_list_view(request):
#     posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'posts_list': posts_list})

# class-based view for post_list_view method
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('datetime_modified')


# def post_detail_view(request, pk):
#     sample_post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': sample_post})

# class-based view for post_detail_view method
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# def post_create_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:  # GET request
#         form = NewPostForm()
#     return render(request, 'blog/post_create.html', context={'form': form})

# class-based view for post_create_view method
class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm  # no () as we need a class not an object
    template_name = 'blog/post_create.html'


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#     return render(request, 'blog/post_create.html', context={'form': form})

# class-based view for post_update_view method
class PostUpdateView(generic.UpdateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'
    model = Post


# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/post_delete.html', context={'post': post})

# class-based view for post_delete_view method
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')

