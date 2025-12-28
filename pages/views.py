from django.shortcuts import render

# Create your views here.
# pages/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # In a real project, you'd send an email.
        # For now, we'll just show a success message.
        # send_mail(
        #     f'Message from {name}',
        #     message,
        #     email,
        #     ['your-email@example.com'],
        # )
        
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return render(request, 'pages/contact.html')
    
    return render(request, 'pages/contact.html')