from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.

class Supplier(models.Model):
    #user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length = 250, null=False)
    phone = models.CharField(max_length = 250, null=False)
    email = models.EmailField(max_length= 250, null=True, blank=True)
    address =  models.CharField(max_length=250,blank=True,null=True)     
    date_created = models.DateTimeField(auto_now_add=True)
    #porfile_pic = models.ImageField(null=True,default="logo.png",blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
    )
    name = models.CharField(max_length=250, null=False)
    price = models.FloatField(null=False, default=0)
    quantity = models.IntegerField(null=False)    
    date_created = models.DateTimeField(auto_now_add=True,null=True)    

    def __str__(self):
        return self.name


class Payment(models.Model):
    STATUS=(
        ('Partial','Partial'),
        ('Complete','Complete'),        
        ('Overdue','Overdue'),
        ('Advance','Advance'),
    )

    PAYMENT_MODE = (
        ('Cash','Cash'),
        ('Netbanking','Netbanking'),
        ('Debitcard','Debitcard'),
        ('Creditcard','Creditcar'),

    )

    TRANSACTION_TYPE = (
        ('Credit','Credit'),
        ('Debit','Debit')
    )

    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
    #product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    bill_number = models.CharField(max_length=250,blank=False, null=False)    
    payment_done = models.FloatField(blank=False, null=False, default=0,validators=[MinValueValidator(0.00)])
    transaction_type = models.CharField(null=False, blank=False, default=TRANSACTION_TYPE[0][0],choices=TRANSACTION_TYPE,max_length=10)
    #payment_mode = models.CharField(max_length=250, null=False, choices=PAYMENT_MODE)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    status = models.CharField(max_length=250, null=False, choices=STATUS, default=STATUS[0][0])
    
    def __str__(self):
        return str(self.bill_number)


