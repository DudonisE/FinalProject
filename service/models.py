from django.contrib.auth.models import User
from django.db import models

from validators import validate_positive

SERVICE_CHOICES = [
    ('Clothing dyeing', 'Clothing dyeing'),
    ('Tailoring', 'Tailoring'),
    ('Alteration', 'Alteration'),
    ('Sewing Pillows or Cushions', 'Sewing Pillows or Cushions'),
]

STATUS = [
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('In progress', 'In progress'),
    ('Shipped', 'Shipped'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
    ('Refunded', 'Refunded'),

]


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, choices=SERVICE_CHOICES)
    price = models.FloatField(verbose_name='Price', blank=False, null=True, validators=[validate_positive])
    status = models.CharField(max_length=200, choices=STATUS)


