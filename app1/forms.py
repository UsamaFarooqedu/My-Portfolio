from django import forms
from .models import Client, Contact
from django.core.validators import MinLengthValidator, EmailValidator
from django.core.exceptions import ValidationError

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'project', 'date', 'description', 'image', 'website']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Client Name'
            }),
            'project': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project Name'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Project description...',
                'rows': 3
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'image': 'Client/Project Image',
            'website': 'Website URL'
        }

def clean_name(self):
    name = self.cleaned_data.get('name')
    if name is None:  # Check if name is None
        raise forms.ValidationError("Name cannot be empty")
    if len(name.strip()) == 0:  # Check if name is empty after stripping whitespace
        raise forms.ValidationError("Name cannot be empty")
    return name

def clean_website(self):
    website = self.cleaned_data.get('website')
    if website and not website.startswith(('http://', 'https://')):
        raise ValidationError("Please enter a valid URL including http:// or https://")
    return website

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1234567890'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your message...',
                'rows': 5
            })
        }
        error_messages = {
            'name': {
                'required': "Please enter your name",
            },
            'email': {
                'required': "Please enter your email",
                'invalid': "Please enter a valid email address"
            },
            'message': {
                'required': "Please enter your message",
            }
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and len(phone) < 10:
            raise ValidationError("Phone number must be at least 10 digits long")
        return phone

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message.split()) < 5:
            raise ValidationError("Message should be at least 5 words long")
        return message