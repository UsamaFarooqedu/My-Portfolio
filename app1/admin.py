from django.contrib import admin
from .models import Head, About, Service, Skill, Client, Contact

class HeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created','image', 'file')
    search_fields = ('name', 'title')
    list_filter = ('created',)
    date_hierarchy = 'created'

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'education', 'year', 'image')
    search_fields = ('title', 'education')
    list_filter = ('year',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'description' ,'proficiency')
    search_fields = ('title',)
    list_editable = ('proficiency',)
    list_filter = ('proficiency',)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'date','project', 'website')
    search_fields = ('name', 'project')
    list_filter = ('date',)
    date_hierarchy = 'date'
    readonly_fields = ('display_image',)
    
    def display_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="150" height="auto" />'
        return "No Image"
    display_image.allow_tags = True
    display_image.short_description = 'Preview'

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'is_read')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('is_read', 'created_at')
    date_hierarchy = 'created_at'
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)

# Register your models here
admin.site.register(Head, HeadAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contact, ContactAdmin)
