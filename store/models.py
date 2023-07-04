from django.contrib.auth.models import User
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


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(BaseModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='product', null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}:{}".format(self.product.name, self.pk)

    def update_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()

    def total_cost(self):
        return self.quantity * self.product.price


class Purchase(BaseModel):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    name = models.CharField(max_length=191)
    email = models.EmailField()
    postal_code = models.IntegerField()
    address = models.CharField(max_length=191)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    guest_name = models.CharField(max_length=50, null=True, blank=True)
    guest_email = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return "{}:{}".format(self.pk, self.email)

    def save(self, *args, **kwargs):
        # Calculate the total price based on cart items
        cart_items = self.cart.cartitem_set.all()
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        self.total_price = total_price

        super().save(*args, **kwargs)

    # def total_cost(self):
    #     return sum([ li.cost() for li in self.lineitem_set.all() ] )
