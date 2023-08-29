from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField

# Create your models here.


class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    reported_item = GenericForeignKey('content_type', 'object_id')
    reason = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.reporter} on {self.reported_item}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=False
    )
    content = models.TextField()
    image = CloudinaryField('image', default='default_image')
    created_on = models.DateTimeField(auto_now_add=True)
    reports = GenericRelation(Report)

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.slug)])

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    upvibes = models.ManyToManyField(
        User, related_name='upvibed_comments', blank=True)
    reports = GenericRelation(Report)

    def __str__(self):
        return f"Comment on {self.post}"

    def total_upvibes(self):
        return self.upvibes.count()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('profile_pictures', blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):

        return self.user.username
