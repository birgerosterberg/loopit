from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile


User = get_user_model()


@receiver(post_save, sender=User)
def create_and_save_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


@receiver(pre_save, sender=User)
def username_to_lower(sender, instance, **kwargs):
    instance.username = instance.username.lower()
