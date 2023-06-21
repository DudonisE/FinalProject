from django.contrib.auth.models import User
from django.db import models

from validators import validate_positive


SERVICE_CHOICES = [
    ('Clothing dyeing', 'Clothing dyeing'),
    ('Tailoring', 'Tailoring'),
    ('Alteration', 'Alteration'),
    ('Sewing Pillows or Cushions', 'Sewing Pillows or Cushions'),
]


class Service(models.Model):
    title = models.CharField(verbose_name='Service', max_length=200, blank=False)
    price = models.FloatField(verbose_name='Price', blank=False, null=True, validators=[validate_positive])

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(to='Service', on_delete=models.CASCADE, verbose_name='Service', null=True)
    date = models.DateTimeField(verbose_name='Date', auto_now_add=True)
    quantity = models.IntegerField(verbose_name="Quantity")

    STATUS = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('In progress', 'In progress'),
        ('Shipped', 'Shipped'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Refunded', 'Refunded'),
    ]
    status = models.CharField(verbose_name='Status', max_length=200, choices=STATUS, blank=True, default='Pending')

    def __str__(self):
        return f'{self.user} | {self.date.strftime("%Y-%m-%d %H:%M:%S")}'


class OrderReview(models.Model):
    order = models.ForeignKey(to="Service", on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(to=User, verbose_name="User", on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    content = models.TextField(verbose_name='Text', max_length=5000)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-date_created']
