from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import get_template  
from django.template import Context
from django.views.generic import ListView, DetailView 
from .models import Oportunity
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, 'home.html', {})

def contact(request):

    if request.method == "POST":

        txt = get_template('contact_form.txt')

        message_name = request.POST['message_name']    
        message_email = request.POST['email']   
        message_subject = request.POST['subject'] 
        message = request.POST['message']

        # subject = message_name + ": " + message_subject

        content = {

            'message_name' : request.POST['message_name'],    
            'message_email' : request.POST['email'],   
            'message_subject' : request.POST['subject'], 
            'message' : request.POST['message'],

        }

        content = txt.render(content)


        send_mail(
            "Novo contacto de email", # subject
            content, # message
            "Site Hightech" + '', # from email
            ['andredamaso96@gmail.com'], # to email
            fail_silently=False
        )

        # return render(request, 'contact.html', {'message_name': message_name})
        # return HttpResponse({'message_name': message_name})
        #return HttpResponse('')
        return HttpResponseRedirect(request.path)
        # return Http
    
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

# def oportunity(request):
#     return render(request, 'oportunity.html', {})

class oportunityView(ListView):
    model = Oportunity
    template_name = 'oportunity.html'

class jobView(DetailView):
    model = Oportunity
    template_name = 'job.html'


def appointment(request):

    if request.method == "POST":

        txt = get_template('job_form.txt')

        first_name = request.POST['first_name']    
        last_name = request.POST['last_name']    
        email = request.POST['email']   
        phone = request.POST['phone'] 
        message = request.POST['message']
        file = request.FILES['file']
        

        # # subject = message_name + ": " + message_subject

        content = {

            'first_name' : request.POST['first_name'],    
            'last_name' : request.POST['last_name'],    
            'email' : request.POST['email'],   
            'phone' : request.POST['phone'], 
            'message' : request.POST['message'],

        }

        content = txt.render(content)


        email = EmailMessage("CANDIDATURA", content, "Site Hightech" + '', ['andredamaso96@gmail.com'])
        
        
        email.attach(file.name, file.read(), file.content_type)

        email.send()

        return render(request, 'appointment.html', {'first_name': first_name}) 
    else:
        return render(request, 'job.html', {})

