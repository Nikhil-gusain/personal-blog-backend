from django.db import models
from django_quill.fields import QuillField
from PortfolioBackend.Utils.Helpers import Helpers
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from django.utils.text import slugify
# Create your models here.

class Pages(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class About(models.Model):
    sectionTitle = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    designation = models.TextField()
    bio = models.TextField()
    profileImage = models.URLField(max_length=2500)
    details = models.JSONField(default=dict,help_text='{"Phone": "Ph no","Email": "email","Address": "Address","Language": "English, Hindi (Multilingual abilities)"}')
    cvLink = models.URLField(max_length=2500)

class Skills(models.Model):
    name = models.CharField(max_length=200)
    percent = models.IntegerField()

    def __str__(self):
        return self.name

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(unique=True,max_length=300,null = True,blank=True)
    excerpt = models.TextField(help_text="Meta description for the blog post")
    coverImage = models.URLField(max_length=2500, blank=True, null=True)
    temp_image = models.ImageField(upload_to='temp/', blank=True, null=True)
    content = QuillField()
    readMin = models.IntegerField(default=0)
    category = models.ForeignKey(Skills, on_delete=models.SET_NULL, null=True,related_name="skillBlog")
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
    # Auto-generate slug if not set
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            num = 1

            # Ensure slug is unique
            while Blogs.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1

            self.slug = unique_slug

        # Calculate read time
        self.readMin = Helpers.CalculateReadingTime(self.content.html)

        super().save(*args, **kwargs)

        # Handle Google Drive upload
        if self.temp_image:
            gdrive_url = Helpers.uploadToDrive(
                file_path=self.temp_image.path,
                file_name=self.temp_image.name,
                folder_id='1E4WMmR5g8GIiT6DLrndCtoJTFqSwcgM2'
            )
            self.coverImage = gdrive_url
            self.temp_image.delete(save=False)

            super().save(*args, **kwargs)


class SkillSection(models.Model):
    sectionTitle = models.CharField(max_length=200)
    intro = models.TextField()
    skills = models.ManyToManyField(Skills, blank=True)

    def __str__(self):
        return self.sectionTitle
    

class Services(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=2500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class ServiceSection(models.Model):
    title = models.CharField(max_length=200,help_text="What I <span class='text-yellow-500'>Provide</span>\n Add span tag with tailwing to highlight")
    subtitle = models.CharField(max_length=200,help_text="Must be uppercase")
    services = models.ManyToManyField(Services, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.subtitle = self.subtitle.upper()
        super().save(*args, **kwargs)

class SocialLinks(models.Model):
    icon = models.CharField(max_length=200)
    url = models.URLField(max_length=2500)

    def __str__(self):
        return self.icon

    
class ContactSection(models.Model):
    title = models.CharField(max_length=200)
    info = models.JSONField(default=dict,help_text='[\n \{\n      "label": "Address",\n      "value": "New Delhi, Delhi, India",\n      "icon": "map-pin"\n    \}' )
    socialLinks = models.ManyToManyField(SocialLinks, blank=True)

    def __str__(self):
        return self.title
    