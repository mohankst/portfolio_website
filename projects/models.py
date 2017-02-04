from django.db import models

# Create your models here.
class Project(models.Model):
		title = models.CharField(max_length=255)
		description = models.TextField(null=True, blank = True)

		def __str__ (self):
			return self.title


class Image(models.Model):
	title = models.CharField(max_length=255)
	project_image = models.ImageField(blank=True, null=True)
	project = models.ForeignKey(Project)

	def __str__(self):
		return self.title