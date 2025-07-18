from django.shortcuts import render, redirect, HttpResponse
from .models import Head, About, Service, Skill, Client
from .forms import ClientForm, ContactForm
from django.contrib import messages
from django.db import IntegrityError 


def home(request):
    head = Head.objects.first()
    about = About.objects.first()
    services = Service.objects.all()[:6]
    skills = Skill.objects.all()[:8]
    clients = Client.objects.all()[:6]
    
    context = {
        'head': head,
        'about': about,
        'services': services,
        'skills': skills,
        'clients': clients,
    }
    return render(request, 'portfolio/home.html', context)


def about(request):
    about = About.objects.first()
    services = Service.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'about': about,
        'services': services,
        'skills': skills,
    }
    return render(request, 'portfolio/about.html', context)


def projects(request):
    clients = Client.objects.all()
    form = ClientForm()
    
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Client added successfully!")
                return redirect('projects')
            except IntegrityError:
                messages.error(request, "A client with these details already exists.")
    
    context = {
        'clients': clients,
        'form': form,
    }
    return render(request, 'portfolio/projects.html', context)


def contact(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent!")
            return redirect('contact')
    
    context = {
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)


def add_client(request):
    try:
        if request.method == 'POST':
            form = ClientForm(request.POST, request.FILES)
            
            try:
                # Check if all fields are empty
                all_empty = True
                for field in form.fields:
                    if field in request.POST and request.POST.get(field, '').strip():
                        all_empty = False
                        break
                
                if all_empty:
                    messages.error(request, "All fields are empty. Please fill at least one field.")
                elif form.is_valid():
                    try:
                        client = form.save(commit=False)
                        # Ensure name is not None before saving
                        if client.name is None or not client.name.strip():
                            messages.error(request, "Name cannot be empty")
                        else:
                            client.save()
                            messages.success(request, "Client added successfully!")
                            return redirect('projects')
                    except IntegrityError:
                        messages.error(request, "A client with these details already exists.")
                    except Exception as e:
                        messages.error(request, f"Could not save client: {str(e)}")
                else:
                    messages.error(request, "Please correct the errors below.")
            except ValueError as e:
                messages.error(request, "Invalid data received.")
            except Exception as e:
                messages.error(request, f"Error processing your request: {str(e)}")
        else:
            form = ClientForm()
        
        return render(request, 'add_client.html', {'form': form})
    
    except Exception as e:
        messages.error(request, "An unexpected error occurred. We've been notified.")
        # Log the error here for debugging
        print(f"Unexpected error: {str(e)}")
        return redirect('home')


def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Your message has been sent successfully!")
                return redirect('contact')
            except IntegrityError:
                messages.error(request, "This contact information already exists.")
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/contact.html', {'form': form})