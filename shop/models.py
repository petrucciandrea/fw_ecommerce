from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, blank=True)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    description = models.CharField(max_length=10000, blank=True, db_index=True)
    price = models.FloatField(default=0)
    image = models.CharField(max_length=350, default='https://placehold.co/400x200?text=default', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200, db_index=True, blank=True)
    state = models.BooleanField(default=False)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    review_star = models.PositiveIntegerField(null=True, blank=True)
    review_text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 5)])
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.item.name}"
