from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template  
from django.template import Context 


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

        return render(request, 'contact.html', {'message_name': message_name}) 
    
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

def oportunity(request):
    return render(request, 'oportunity.html', {})