from django.contrib.auth.models import User
from django.db import models
from user.models import Profile


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
    description = models.TextField(max_length=200, blank=True)

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
    description = models.CharField(max_length=500)
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


class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField(default=1, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return "{}:{}".format(self.product.name, self.id)

    def update_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()

    def total_cost(self):
        return self.quantity * self.price


class Order(models.Model):
    name = models.CharField(max_length=191)
    email = models.EmailField()
    postal_code = models.IntegerField()
    address = models.CharField(max_length=191)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{}".format(self.id, self.email)

    # def total_cost(self):
    #     return sum([ li.cost() for li in self.lineitem_set.all() ] )
