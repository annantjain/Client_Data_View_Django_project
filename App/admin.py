from django.contrib import admin
from .models import Customer, Category, Location,Contact

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Contact)