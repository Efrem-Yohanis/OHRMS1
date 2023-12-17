from django.db import models
from django.contrib.auth.models import User

class unapproved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    activation = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='Profile_pic/', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ListingHouse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings', null=True)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    description = models.TextField()
    image1 = models.ImageField(upload_to='listings/')
    image2 = models.ImageField(upload_to='listings/', blank=True)
    image3 = models.ImageField(upload_to='listings/', blank=True)
    image4 = models.ImageField(upload_to='listings/', blank=True)
    approval = models.BooleanField(blank=True, null=True, default=False)
    crated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
class BookingHouse(models.Model):
   
    REQUEST_STATUS_CHOICES = [
        ('REQUEST_APPROVED', 'Request Approved'),
        ('REQUEST_REJECTED', 'Request Rejected'),
        ('REQUEST_ON_PROCESS', 'Request On Process'),
        ('REQUEST_COMPLETED', 'Request Completed'),
    ]
    Request_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_booking', null=True)
    house_info = models.ForeignKey(ListingHouse, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100, blank=True, null=True,choices=REQUEST_STATUS_CHOICES,default='REQUEST_ON_PROCESS')
    crated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    