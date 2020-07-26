from django.urls import path
from . import views
from .views import oportunityView, jobView

urlpatterns = [
   path('', views.home, name="home"),
   path('contact.html', views.contact, name="contact"),
   path('about.html', views.about, name="about"),
   path('services.html', views.services, name="services"),
   path('oportunity.html', oportunityView.as_view(), name="oportunity"),
   path('job/<int:pk>', jobView.as_view(), name="job"),
   path('appointment.html', views.appointment, name="appointment"),
   # path('oportunity.html', views.oportunity, name="oportunity"),
   
]
