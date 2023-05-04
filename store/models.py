from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


CHOICES = [
    ('Man', 'Man'),
    ('Woman', 'Woman'),
    ('Kids', 'Kids'),
]

SIZE_CHOICES = [
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
]


class Size(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)


class Category(BaseModel):
    category_name = models.CharField(max_length=50, choices=CHOICES)
    description = models.CharField(max_length=500)


class Products(BaseModel):
    name = models.CharField(max_length=100, blank=False)
    color = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500)
    category_name = models.ManyToManyField(Category)
    size = models.ManyToManyField(Size)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image_1 = models.ImageField(upload_to="product_images", default=None, blank=False)
    image_2 = models.ImageField(upload_to="product_images", default=None)
    image_3 = models.ImageField(upload_to="product_images", default=None)
