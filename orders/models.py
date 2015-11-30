from django.db import models
from contractors import models as contractors

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from datetime import date


# Create your models here.
class Order(models.Model):
    date = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    fromContractor = models.ManyToManyField(contractors.Contractor, blank=True, related_name='fromContractor')
    toContractor = models.ManyToManyField(contractors.Contractor, blank=True, related_name='toContractor')
    type = models.CharField(max_length=20)

    @property
    def total(self):
        orderItems = OrderItem.objects.filter(order=self).values_list('price', 'quantity')
        return sum ([int(price)*int(quantity) for price, quantity in orderItems])


class OrderItem(models.Model):
    name = models.CharField(max_length=200)
    order = models.ForeignKey(Order, related_name='item')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    unitOfMeasure = models.CharField(max_length=20)

