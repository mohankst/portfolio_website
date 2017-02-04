from django.contrib import admin

from .models import Project, Image

class ImageInline(admin.StackedInline): #adding the ability to upload images with a Project
	model = Image

class ProjectAdmin(admin.ModelAdmin): #Admin for handling Projects
	inlines = [ImageInline,]

admin.site.register(Project, ProjectAdmin)