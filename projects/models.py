from django.db import models
from django.db.models.signals import pre_save

from django.utils.text import slugify
# Create your models here.
class Project(models.Model):
		title = models.CharField(max_length=255)
		slug = models.SlugField(unique=True)
		description = models.TextField(null=True, blank = True)

		def __str__ (self):
			return self.title


class Image(models.Model):
	title = models.CharField(max_length=255)
	project_image = models.ImageField(blank=True, null=True)
	project = models.ForeignKey(Project)

	def __str__(self):
		return self.title

#Creating auto slug field
def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_project_recever(sender, instance, *args, **kwargs):
	if not instanc.slug:
		instanc.slug = create_slug


pre_save.connect(pre_save_project_recever, sender=Project)