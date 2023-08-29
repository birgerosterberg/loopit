from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post, Comment
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


class CreatePostView(LoginRequiredMixin, View):
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

# Apply the login_required decorator to make sure
# only logged-in users can access the view.


@method_decorator(login_required, name='dispatch')
class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, View):
    """View to handle the deletion of a user's own posts."""

    template_name = 'delete_post.html'

    def test_func(self):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return post.author == self.request.user

    def get(self, request, slug):
        """
        Handle GET requests.

        Show a confirmation page for deleting the post.
        """
        # Fetch the Post object based on the slug and make
        # sure the author matches the logged-in user.
        post = get_object_or_404(Post, slug=slug, author=request.user)
        return render(request, DeletePostView.template_name, {'post': post})

    def post(self, request, slug):
        """
        Handle POST requests.

        Delete the post and redirect to the homepage.
        """
        # Fetch the Post object based on the slug and
        # make sure the author matches the logged-in user.
        post = get_object_or_404(Post, slug=slug, author=request.user)
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        # Redirect to the post list after deletion.
        return redirect('home')


# Apply the login_required decorator to make sure only
# logged-in users can access the view.
@method_decorator(login_required, name='dispatch')
class EditPostView(LoginRequiredMixin, UserPassesTestMixin, View):
    """View to handle editing a user's own posts."""

    template_name = 'edit_post.html'

    def test_func(self):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return post.author == self.request.user

    def get(self, request, slug):
        """
        Handle GET requests.

        Render a form for editing the post,
        pre-filled with the current post information.
        """
        # Fetch the Post object based on the slug and make sure
        # the author matches the logged-in user.
        post = get_object_or_404(Post, slug=slug, author=request.user)
        form = PostForm(instance=post)
        return render(
            request, EditPostView.template_name, {'form': form, 'post': post}
        )

    def post(self, request, slug):
        """
        Handle POST requests.

        Update the post if the submitted form is valid.
        Redirect to the post detail view afterwards.
        """
        # Fetch the Post object based on the slug and
        # make sure the author matches the logged-in user.
        post = get_object_or_404(Post, slug=slug, author=request.user)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', slug=post.slug)
        return render(
            request, EditPostView.template_name, {'form': form, 'post': post}
        )

# Use the @method_decorator to apply the login_required decorator to the View class.
# This ensures that only logged-in users can access the view.


@method_decorator(login_required, name='dispatch')
class MyProfileView(View):
    """View to display the logged-in user's profile."""

    template_name = 'my_profile.html'

    def get(self, request):
        """
        Handle GET requests.

        Render the user's profile using the 'my_profile.html' template.
        """
        return render(
            request, self.template_name, {
                'user_profile': request.user.userprofile}
        )


# Again, apply the login_required decorator to make sure only logged-in
# users can access the view.
@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    """View to handle editing the logged-in user's profile."""

    template_name = 'edit_profile.html'

    def get(self, request):
        """
        Handle GET requests.

        Render a form for editing the user's profile, pre-filled
        with the current profile information.
        """
        form = UserProfileForm(instance=request.user.userprofile)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        Handle POST requests.

        Update the user's profile if the submitted form is valid.
        Redirect to the profile view afterwards.
        """
        # This line handles both POST data and FILES (i.e., the uploaded image)
        form = UserProfileForm(request.POST, request.FILES,
                               instance=request.user.userprofile)

        if form.is_valid():
            form.save()
            return redirect('my_profile')
        return render(request, self.template_name, {'form': form})


class UserProfileView(View):
    """View to display any user's profile based on the username in the URL."""

    template_name = 'user_profile.html'

    def get(self, request, username):
        """
        Handle GET requests.

        Render the profile of the user specified by the 'username'
        argument in the URL.
        """
        # Fetch the User object corresponding to the username.
        # If it doesn't exist, return a 404 error.
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
