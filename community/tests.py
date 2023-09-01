from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Category

# Create your tests here.


class PostViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Setup Test Data: Creating user, category, and post...")  # Added print
        # Create a user
        user_model = get_user_model()
        cls.user = user_model.objects.create_user(
            username='testuser', password='thisissosaf3')

        # Create a category
        cls.category = Category.objects.create(name='TestCategory')

        # Create a post
        cls.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=cls.user,
            category=cls.category
        )

    def test_non_logged_in_user_edit_post(self):
        print("Test Start: Non-logged-in user trying to edit a post...")

        # Generate the URL for edit_post view
        url = reverse('edit_post', kwargs={'slug': self.post.slug})

        # Make a GET request to the edit_post URL
        response = self.client.get(url)

        print("Verifying the redirect to the login page...")
        # Check if the response redirects to the login page
        self.assertRedirects(response, f'/accounts/login/?next={url}')
        print("Test Success: Redirected to login page as expected.")

    def test_non_logged_in_user_delete_post(self):
        print("Test Start: Non-logged-in user trying to delete a post...")

        # Generate the URL for delete_post view
        url = reverse('delete_post', kwargs={'slug': self.post.slug})

        # Make a GET request to the delete_post URL
        response = self.client.get(url)

        print("Verifying the redirect to the login page...")
        # Check if the response redirects to the login page
        self.assertRedirects(response, f'/accounts/login/?next={url}')
        print("Test Success: Redirected to login page as expected.")
