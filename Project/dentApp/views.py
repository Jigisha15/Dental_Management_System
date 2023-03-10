from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib import messages  
from dentApp.models import Appointment
from dentApp.forms import PatientRegistrationForm, ContactForm
from django.core.mail import send_mail, EmailMessage
from django.views.generic import ListView
import datetime
from django.template.loader import render_to_string, get_template
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# this is for appointment of Patient 
class AppointmentTemplateView(TemplateView):
    template_name = 'appointment.html'
    @login_required

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')
        date = request.POST.get('date')
        time = request.POST.get('time')


        appointment = Appointment.objects.create(
            name=name,
            email=email,
            number=number,
            content=content,
            date=date,
            time=time
        )
        appointment.save()
        messages.add_message(request, messages.SUCCESS, f"Thanks {name} for making an appointment. We will email you ASAP!")
        return redirect('appointment')



def blog(request):
    return render(request, 'blog.html')


# this is for managing appointments
class ManageAppointmentTemplateView(ListView):
    template_name = 'manageapp.html'
    model = Appointment
    context_object_name = 'appointments'
    login_required = True
    paginate_by = 3

    @user_passes_test(lambda u: u.is_superuser)
    def post(self, request):
        date = request.POST.get('date')
        appointment_id = request.POST.get('appointment-id')
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            'name':appointment.name,
            'date':date
        }
        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment in Trutle\'s Clinic",
            message,
            'cmpn2025@gmail.com',
            [appointment.email],
        )
        email.content_subtype = 'html'
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.name}")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            'title':'Manage Appointments',
        })
        return context


# this is for contact us of Patient 
@login_required
def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('contactemail.html', {
                'name':name,
                'email':email,
                'content':content
            })

            send_mail(
                'Hello from Turtle\'s Clinic. This is an automated email, do not reply.',
                'This is contact form.',
                'noreply@codewithstein.com',
                ['cmpn2025@gmail.com'],
                html_message = html
                # fail_silently=False
            )
        return redirect('contact')
    else:
        form = ContactForm(request.POST)

    return render(request, 'contact.html', {'form':form})

def gallery(request):
    return render(request, 'gallery.html')



# this is for login of patient 
def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user=authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('login')
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('login')
    return render(request, 'login.html')

# this is for logout of Patient 
def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')


def profile(request):
    return render(request, 'profile.html')


# this is for signup of patient
class PatientRegistrationView(View):
    def get(self, request):
        form = PatientRegistrationForm()
        if request.user.is_authenticated:
            pass
        return render(request, 'signup.html', locals())
    def post(self, request):
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User registered successfully!")
        else:
            messages.warning(request, "Inavlid Credentials")
        return render(request, 'signup.html', locals())

def team(request):
    return render(request, 'team.html')

def testimonials(request):
    return render(request, 'testimonials.html')


def services(request):
    return render(request, 'services.html')

def location(request):
    return render(request, 'location.html')

def tnc(request):
    return render(request, 'tnc.html')