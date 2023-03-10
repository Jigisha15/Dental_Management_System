from django.urls import path
from . import views
from dentApp.forms import *
from django.contrib.auth import views as auth_views
# from .forms import LoginForm
from dentApp.views import AppointmentTemplateView, ManageAppointmentTemplateView

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),

    # this is for sending appointment
    path('appointment/', AppointmentTemplateView.as_view(), name="appointment"),
    path('manageapp/', ManageAppointmentTemplateView.as_view(), name="manageapp"),

    path('services/', views.services, name="services"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.gallery, name="gallery"),
    path('location/', views.location, name="location"),
    path('tnc/', views.tnc, name="tnc"),


    # this is for login of Patient 
    path('login/', views.login, name="login"),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),

    # this is for logout of Patient 
    # path('logout/', auth_view.LogoutView.as_view(next_page="login"), name="logout"),
    path('logout/', views.Logout, name="logout"),

    # this is for signup of patient
    path('signup/', views.PatientRegistrationView.as_view(), name="signup"),
    # path('signup/', views.signup, name="signup"),

    # this is for profile of Patient 
    path('profile/', views.profile, name="profile"),

    path('team/', views.team, name="team"),
    path('testimonials/', views.testimonials, name="testimonials"),
]