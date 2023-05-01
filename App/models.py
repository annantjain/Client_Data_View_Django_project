from django.db import models

# Create your models here.
class Location(models.Model):
    state_name = models.CharField(max_length=100, null=False)
    city_name = models.CharField(max_length=100)
    def __str__(self): 
        return self.state_name +" "+ self.city_name  #returns a string representation of the object which will be vissible to us
    
class Category(models.Model):
    name=models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name   #returns a string representation of the object

class Customer(models.Model):
    first_name = models.CharField(max_length=100, null=False)   # represents a character (string) field for the first name of a customer. It can have a maximum length of 100 characters.

    last_name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    total_shopping_amount = models.IntegerField(default=0)
    preffered_shopping_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    last_shoped_date = models.DateTimeField()
    
    def __str__(self):
        return "%s %s %s" %(self.first_name , self.last_name , self.phone)      #the string representation includes the first_name, last_name, and phone attributes of an object, separated by spaces.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=18)