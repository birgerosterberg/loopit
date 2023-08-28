from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post, UserProfile, Comment
from .forms import PostForm, CommentForm, UserProfileForm, ReportForm


class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_on')
        category_name = self.request.GET.get('category')
        if category_name:
            queryset = queryset.filter(category__name=category_name)
        return queryset


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


@method_decorator(login_required, name='dispatch')
class MyProfileView(View):
    template_name = 'my_profile.html'

    def get(self, request):
        return render(request, self.template_name, {'user_profile': request.user.userprofile})


@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    template_name = 'edit_profile.html'

    def get(self, request):
        form = UserProfileForm(instance=request.user.userprofile)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
        return render(request, self.template_name, {'form': form})


class UserProfileView(View):
    template_name = 'user_profile.html'

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        print(f"Username: {username}, User object: {user}")  # Debugging line
        return render(request, self.template_name, {'user_profile': user.userprofile})


class ReportItemView(View):
    """View for reporting posts or comments."""

    template_name = 'report_form.html'
    http_method_names = ['get', 'post']

    def get(self, request, content_type, object_id):
        """
        Handle GET requests to display the report form.

        Args:
            request: The HTTP request object.
            content_type: Type of content ('post' or 'comment').
            object_id: ID of the content to report.

        Returns:
            Rendered HTML template with the report form.
        """
        content_map = {
            'post': Post,
            'comment': Comment,
        }
        content_class = content_map.get(content_type)
        content_item = get_object_or_404(content_class, id=object_id)
        form = ReportForm(
            initial={'content_type': content_type, 'object_id': object_id})
        print(f"Debug: content_type = {content_type}, object_id = {object_id}")
        context = {'form': form, 'content_item': content_item}
        return render(request, self.template_name, context)

    def post(self, request, content_type, object_id):
        """
        Handle POST requests to submit a report.

        Args:
            request: The HTTP request object.
            content_type: Type of content ('post' or 'comment').
            object_id: ID of the content being reported.

        Returns:
            Redirect to home page with a success message if report is valid,
            otherwise re-renders the report form with error messages.
        """
        content_map = {
            'post': Post,
            'comment': Comment,
        }
        content_class = content_map.get(content_type)
        content_item = get_object_or_404(content_class, id=object_id)
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.reported_item = content_item
            report.save()

            # Display a success message and redirect to home page
            messages.success(request, 'Report submitted successfully.')
            return redirect('home')

        context = {'form': form, 'content_item': content_item}
        return render(request, self.template_name, context)
