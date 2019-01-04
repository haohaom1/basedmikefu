from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, 'mysite/index.html')

def project(request):
    return render(request, 'mysite/project.html')

def experience(request):
    return render(request, 'mysite/experience.html')

def contact(request):

    # either a POST or a GET method
    # a GET method is to retrieve something from the server
    # a POST method is to send something to the server
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        # saves the information into the database
        c = Contact(email=email_r, message=message_r, subject=subject_r)
        c.save()

    return render(request, 'mysite/contact.html')
