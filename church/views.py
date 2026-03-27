from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'church/home.html')

def about(request):
    return render(request, 'church/about.html')

def visit(request):
    return render(request, 'church/visit.html')

def contact(request):
    return render(request, 'church/contact.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send email (optional - requires email configuration)
        # send_mail(
        #     f'Contact Form Message from {name}',
        #     f'From: {name}\nEmail: {email}\n\nMessage:\n{message}',
        #     settings.DEFAULT_FROM_EMAIL,
        #     ['info@caacc.org.au'],
        #     fail_silently=False,
        # )
        
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('contact')
    
    return render(request, 'church/contact.html')



def english(request):
    return render(request, 'church/english.html')

def cantonese(request):
    return render(request, 'church/cantonese.html')


def get_connected(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        group_type = request.POST.get('group_type')
        location = request.POST.get('location')
        
        messages.success(request, f'Thank you {name}! We will contact you soon about joining a Life Group.')
        return redirect('get_connected')
    
    return render(request, 'church/get-connected.html')

def serve_others(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        interests = request.POST.getlist('interest')
        
        messages.success(request, f'Thank you {name}! We will contact you soon about serving opportunities.')
        return redirect('serve_others')
    
    return render(request, 'church/serve-others.html')

