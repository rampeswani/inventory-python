# models.py
from django.db import models
from django.contrib.auth.models import User

class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.CharField(max_length=255)

    def __str__(self):
        return self.data

class CustomerType(models.Model):
    customer_type_id = models.AutoField(primary_key=True)
    customer_type_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.customer_type_id )
    class Meta :
        ordering = ['customer_type_id']
    

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_name_hindi = models.CharField(max_length=200)
    customer_fathers_name = models.CharField(max_length=100)
    customer_fathers_name_hindi = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=500)
    customer_contact_number = models.CharField(max_length=10)
    credit_amount = models.DecimalField(decimal_places=2,max_digits=10)
    customerType = models.ForeignKey(CustomerType , on_delete=models.CASCADE,related_name='customer_customer_type')
    description = models.TextField()




    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='customer_user_set')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='customer_created_by_set')
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank=True,related_name='customer_updated_by_set')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True,null=True,blank=True)
    created_IP = models.CharField(max_length=100,null= True,blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['customer_id']

    def __str__(self):
        return str(self.customer_id)