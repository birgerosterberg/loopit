from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post
from .forms import PostForm
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 10


class CreatePostView(View):
    template_name = 'create_post.html'

    def get(self, request):
        form = PostForm()
        return render(request, CreatePostView.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', slug=post.slug)
        return render(request, CreatePostView.template_name, {'form': form})


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        post = Post.objects.get(slug=slug)
        comments = post.comments.order_by('-created_on')
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        post = Post.objects.get(slug=slug)
        comments = post.comments.order_by('-created_on')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )


@method_decorator(login_required, name='dispatch')
class DeletePostView(View):
    template_name = 'delete_post.html'

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        return render(request, DeletePostView.template_name, {'post': post})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        post.delete()
        # Redirect to the post list after deletion
        return redirect('home')
