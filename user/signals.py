from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, BodyMeasurements


"""
Function create_profile is a signal handler that gets triggered after a User object is saved. 
It creates a related Profile and BodyMeasurements object associated with the user instance that was just created.
"""


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        BodyMeasurements.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.bodymeasurements.save()

