from django.shortcuts import render, HttpResponse
from .models import Customer, Location, Category
from datetime import datetime, timedelta
from django.db.models import Q
import pytz
from django.utils import timezone
from django.contrib import messages
from App.models import Contact

#importing librairies

# Create your views here.


def index(request):
    return render(request, 'index.html') #rendering the index.html template and returns it as an HTTP response to the user's request.


def all_cust(request):
    custs = Customer.objects.all()
    # Command To view All item in a model where Customer is a model
    context = {
        'custs': custs
    }
    # context is a variable name -> variable value mapping that is passed to template(written in JSON format)
    return render(request, 'all_cust.html', context)
    # rendering all_cust template with variable context


def add_cust(request):

    if request.method == 'POST': # conditional statement that checks whether the request method is POST or not. In HTTP, POST is a request method used by clients to submit data to the server.

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        preffered_shopping_category = request.POST['preffered_shopping_category']
        location = request.POST['location']
        phone = int(request.POST['phone'])
        total_shopping_amount = int(request.POST['total_shopping_amount'])
        #retrieving the value of the input field from the HTTP POST request data.


        new_cust = Customer(first_name=first_name, last_name=last_name, location=location, email=email, total_shopping_amount=total_shopping_amount,preffered_shopping_category=preffered_shopping_category, phone=phone,last_shoped_date = datetime.now())
        #creating a new instance of the Customer model new_cust with the given attribute values

        new_cust.save() #saving the new_cust in database

        return HttpResponse('Customer added successfully')
    
    elif request.method == 'GET':         
        return render(request, 'add_cust.html') 
    else:
        return HttpResponse("Exception Occured ! Customer not added successfully")
    #If the HTTP request method is 'GET', it returns a rendered HTML template named 'add_cust.html' to the client.If not then returns an error message

def filter_cust(request):

    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        preffered_shopping_category = request.POST['preffered_shopping_category']
        #retrieving the value of the input field from the HTTP POST request data.

        custs = Customer.objects.all()
        # Command To view All item in a model where Customer is a model
        
        if name:
            custs = custs.filter(Q(first_name__icontains=name)
                                 | Q(last_name__icontains=name))
        #filtering the queryset of customers based on the name parameter received in the request. If name is not empty, it uses the Django Q object to filter the customers whose first name or last name contain the name string (case-insensitive) using the icontains lookup. 
            


        if location:
            custs = custs.filter(location__state_name__icontains=location)
        if preffered_shopping_category:
            custs = custs.filter(
                preffered_shopping_category__name__icontains=preffered_shopping_category)
            #filtering the queryset of customers based on the location parameter and preffered_shopping_category 


        context = {
            'custs': custs
        }
        return render(request, 'all_cust.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_cust.html')
    else:
        return HttpResponse('An Exception occured')
# same meaning as of previous method

def remove_cust(request, cust_id=0):  #The cust_id parameter is optional and defaults to 0 if not specified in the request.

    if cust_id:
        try:
            cust_removed = Customer.objects.get(id=cust_id)
            cust_removed.delete()
            return HttpResponse("Customer Removed Successfully")      #checking if a customer ID is provided or not. If the customer ID is provided, it tries to retrieve the corresponding customer object from the database and delete it using the delete() method.
        except:
            return HttpResponse("Please enter a valid Customer ID")
    custs = Customer.objects.all()
    context = {
        'custs': custs
    }
    return render(request, 'remove_cust.html', context)
#already described before


def is_active(request):
    X_Days = 120
    custs = Customer.objects.all()
    active_custs = []
    for cust in custs:
        if cust.last_shoped_date >= (timezone.now() - timedelta(days=X_Days)):
            active_custs.append(cust)  
            #timezone.now() returns the current datetime according to the timezone set in the Django settings
            #checking if the last shoped date of a customer is smaller than X days. If it is smaller then it is active user

 
    context = {
        'custs': active_custs
    }
    return render(request, 'is_active.html', context)

def is_inactive(request):
    X_Days = 120
    custs = Customer.objects.all()
    inactive_custs = []
    for cust in custs:
        if cust.last_shoped_date < (timezone.now() - timedelta(days=X_Days)):
            inactive_custs.append(cust) #checking if the last shoped date of a customer is greater than X days. If it is greater then it is inactive user 


    context = {
        'custs': inactive_custs
    }
    return render(request, 'is_inactive.html', context)

def is_potential(request):
    X_Amount = 10000
    custs = Customer.objects.all()
    potential_custs = []
    for cust in custs:
        if cust.total_shopping_amount > X_Amount:
            potential_custs.append(cust)
            #checking if the total shopping amount of a customer is greater than X amount. If it is greater then it is potential user 

    context = {
        'custs': potential_custs
    }
    return render(request, 'is_potential.html', context)


def previous_cust(request):
    X_MONTHS=1
    custs = Customer.objects.all()
    previous_custs = []
    for cust in custs:
        delta = timezone.now()-cust.last_shoped_date
        if delta < timedelta(days=X_MONTHS*30) :
            previous_custs.append(cust)
            #Checking whether the customer has maked shopping in the last X months.If yes then it is a previous customer

    context = {
        'custs': previous_custs
    }
    return render(request, 'previous_cust.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = Contact(name=name, email=email, password=password)
        contact.save()
        messages.success(request, "We will soon reach to you !!") # displaying message on successful submission of contact form

    return render(request, 'contact.html')