from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Patient, Contact, Appointment

# Register your models here.
@admin.register(Patient)
class PatientRegistration(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'state', 'zipcode']

admin.site.register(Appointment)

@admin.register(Contact)
class ContactForm(admin.ModelAdmin):
    list_display = ['name', 'email', 'content']

admin.site.unregister(Group)