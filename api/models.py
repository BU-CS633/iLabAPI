from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    vendor = models.CharField(max_length=200,null=True,blank=True)
    catalog = models.CharField(max_length=255, null=True, blank=True)  # Adding the catalog field
    lastOrderDate = models.DateField(null=True, blank=True)  # Adding the lastOrderDate field
    lastReceivedDate = models.DateField(null=True, blank=True)  # Adding the lastReceivedDate field

    def __str__(self):
        return self.name


class Status(models.Model):
    description = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.description


class Request(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    request_date = models.DateField(null=True,blank=True)
    order_date = models.DateField(null=True,blank=True)
    received_date = models.DateField(null=True,blank=True)
    approved_date = models.DateField(null=True,blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return self.item.name
