from django.db import models
from django.contrib.auth.models import User
from validators import validate_positive


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images', blank=True)

    def __str__(self):
        return f"{self.user.username} profile"


class BodyMeasurements(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bust = models.PositiveIntegerField(verbose_name='Bust', blank=True, null=True)
    waist = models.PositiveIntegerField(verbose_name='Waist', blank=True, null=True)
    hips = models.PositiveIntegerField(verbose_name='Hips', blank=True, null=True, validators=[validate_positive])
    neck = models.PositiveIntegerField(verbose_name='Neck', blank=True, null=True)
    chest = models.PositiveIntegerField(verbose_name='Chest', blank=True, null=True)
    shoulder = models.PositiveIntegerField(verbose_name='Shoulder', blank=True, null=True)
    sleeve = models.PositiveIntegerField(verbose_name='Sleeve', blank=True, null=True)
    shoulder_to_waist = models.PositiveIntegerField(verbose_name='Shoulder to waist', blank=True, null=True)
    shoulder_to_floor = models.PositiveIntegerField(verbose_name='Shoulder to floor',  blank=True, null=True)
    comment = models.TextField(verbose_name="Additional information", max_length=250, blank=True, null=True)
    measure_model = models.ImageField(default='body_measurements.jpg', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} body measurements"


class ContactUs(BaseModel):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    message = models.TextField(max_length=1000, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
