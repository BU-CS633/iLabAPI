from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    description = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.description

class Item(models.Model):
    name = models.CharField(max_length=200)
    fullName = models.CharField(max_length=200,null=True,blank=True)
    unitSize = models.CharField(max_length=200,null=True,blank=True)
    qty = models.IntegerField()
    price = models.FloatField(null=True,blank=True)
    vendor = models.CharField(max_length=200,null=True,blank=True)
    catalog = models.CharField(max_length=255, null=True, blank=True)
    lastOrderDate = models.DateField(null=True, blank=True)
    lastReceivedDate = models.DateField(null=True, blank=True)
    channel = models.CharField(max_length=200,null=True,blank=True)
    location = models.CharField(max_length=200,null=True,blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE,null=True,blank=True)
    link = models.CharField(max_length=200,null=True,blank=True)
    notes = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

class Request(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    request_date = models.DateField(null=True,blank=True)
    order_date = models.DateField(null=True,blank=True)
    received_date = models.DateField(null=True,blank=True)
    approved_date = models.DateField(null=True,blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_owner')
    receivedBy = models.ForeignKey(User, on_delete=models.CASCADE,related_name='request_received_by',null=True,blank=True)

    def __str__(self):
        return self.item.name
