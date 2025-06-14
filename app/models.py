from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Order(models.Model):
    set = models.CharField(max_length=100, default='GOSET')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    main_dish = models.CharField(max_length=100)
    rice = models.CharField(max_length=100, default='Plain Rice')
    side_dish = models.CharField(max_length=100)
    second_side_dish = models.CharField(max_length=100)
    dessert = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.pk} by {self.user.username}"

class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('done', 'Done')))
    set = models.CharField(max_length=15)
    rice = models.CharField(max_length=100)
    main_dish = models.CharField(max_length=100)
    side_dish = models.CharField(max_length=100)
    second_side_dish = models.CharField(max_length=100, blank=True)
    dessert = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)