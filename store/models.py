from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


GENDER_CHOICES = [
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
    size = models.CharField(max_length=200, choices=SIZE_CHOICES)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.size


class Category(BaseModel):
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='notSelected')
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.gender} {self.category_name}'


class Product(BaseModel):
    owner = models.ForeignKey('auth.User', related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    color = models.CharField(max_length=100, blank=False)
    description = models.TextField(verbose_name="Additional information", max_length=500)
    category_name = models.ManyToManyField(Category)
    size = models.ManyToManyField(Size)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image_1 = models.ImageField(upload_to="product_images", default=None, blank=True)
    image_2 = models.ImageField(upload_to="product_images", default=None, blank=True)
    image_3 = models.ImageField(upload_to="product_images", default=None, blank=True)

    def __str__(self):
        return self.name
