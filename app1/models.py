from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

class Head(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='head_images/', blank=True, null=True)
    file = models.FileField(upload_to='head_files/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name if self.name else "Untitled Head"

class About(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)  # Fixed typo from 'eduction'
    year = models.DateField(default=timezone.now)
    image = models.ImageField(
        upload_to='about_images/', 
        blank=True, 
        null=True, 
        help_text="Profile picture"
    )

    def __str__(self):
        return self.title

class Service(models.Model):  # Changed from 'Services' to singular 'Service'
    title = models.CharField(max_length=30, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Services"  # Proper plural name in admin

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    proficiency = models.PositiveIntegerField(
        default=50,
        validators=[
            MinValueValidator(0),  # Minimum value 0
            MaxValueValidator(100)  # Maximum value 100
        ]
    )
    
    def __str__(self):
        return self.title if self.title else "Unnamed Skill"

class Client(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    project = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(default=timezone.now)
    description = models.TextField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='client_images/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)  # Added website URL field

    def __str__(self):
        return f"{self.name} - {self.project}" 

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[MinLengthValidator(10)]
    )
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # Added to track read status

    def __str__(self):
        return f"Message from {self.name} ({self.email})"