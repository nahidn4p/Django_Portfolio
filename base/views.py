from django.shortcuts import render
from django.http import HttpResponse,request
from django.contrib import messages
from .models import Contact
# Create your views here.

# def home(request):
#     return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        number= request.POST.get('number')
        if len(name) < 2 or len(name) > 50:
            messages.error(request, 'Name must be at least 3 characters long.')
            return render(request, 'home.html')
        if len(email) < 5 or len(email) > 50:
            messages.error(request, 'Email must be at least 5 characters long.')
            return render(request, 'home.html') 
        if len(content) < 10 or len(content) > 500:
            messages.error(request, 'Content must be between 10 and 500 characters long.')
            return render(request, 'home.html')
        else:
            # Save the contact form data to the database
            contact = Contact(name=name, email=email, content=content, number=number)   
            contact.save()
            # Show a success message
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
    return render(request, 'home.html')
        
    
