from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post, UserProfile
from .forms import PostForm, CommentForm, UserProfileForm


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
            messages.success(request, 'Post created successfully!')
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
        messages.success(request, 'Post deleted successfully!')
        # Redirect to the post list after deletion
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class EditPostView(View):
    template_name = 'edit_post.html'

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        form = PostForm(instance=post)
        return render(
            request, EditPostView.template_name, {'form': form, 'post': post}
        )

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', slug=post.slug)
        return render(
            request, EditPostView.template_name, {'form': form, 'post': post}
        )


class UserProfileView(View):
    template_name = 'user_profile.html'

    def get(self, request, *args, **kwargs):
        user_profile = request.user.userprofile
        return render(request, 'user_profile.html', {'user_profile': user_profile})


class UpdateUserProfileView(View):
    template_name = 'update_user_profile.html'

    def get(self, request, *args, **kwargs):
        user_profile = request.user.userprofile
        form = UserProfileForm(instance=user_profile)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user_profile = request.user.userprofile
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile_view')
        return render(request, self.template_name, {'form': form})


class ViewUserProfile(View):
    template_name = 'view_user_profile.html'

    def get(self, request, username, *args, **kwargs):
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user=user)
        return render(request, self.template_name, {'user_profile': user_profile})
