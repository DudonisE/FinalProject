from django.db import models

from PIL import Image
from django.contrib.auth.models import User


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.avatar.path)


class BodyMeasurements(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bust = models.FloatField(verbose_name='Bust', max_length=10)
    waist = models.FloatField(verbose_name='Waist', max_length=10)
    hips = models.FloatField(verbose_name='Hips', max_length=10)
    neck = models.FloatField(verbose_name='Neck', max_length=10)
    chest = models.FloatField(verbose_name='Chest', max_length=10)
    shoulder = models.FloatField(verbose_name='Shoulder', max_length=10)
    sleeve = models.FloatField(verbose_name='Sleeve', max_length=10)
    shoulder_to_waist = models.FloatField(verbose_name='Shoulder to waist', max_length=10)
    shoulder_to_floor = models.FloatField(verbose_name='Shoulder to floor', max_length=10)
    comment = models.TextField(verbose_name="Additional information", max_length=250, blank=True)
    measure_model = models.ImageField(default='bodymeasurements.jpg')
    last_updated = models.DateTimeField(auto_now_add=True)


