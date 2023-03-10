from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth.models import User


# Create your models here.
STATE_CHOICES = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chattisgarh', 'Chattisgarh'),
    ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
    ('Daman & Diu', 'Daman & Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujrat', 'Gujrat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisa', 'Odisa'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal'),
)



# this is for signup of patient
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name
    


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    content = models.CharField(max_length=250)


# this is for appointment form of Patient 
class Appointment(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    number = models.CharField(max_length=50, null=True, blank=True)
    content = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    accepted = models.BooleanField(default=False, null=True, blank=True)
    accepted_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
        
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-time']