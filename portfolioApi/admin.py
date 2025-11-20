from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.About)
admin.site.register(models.Blogs)
admin.site.register(models.Skills)
admin.site.register(models.SkillSection)
admin.site.register(models.ServiceSection)
admin.site.register(models.Services)
admin.site.register(models.SocialLinks)
admin.site.register(models.ContactSection)
admin.site.register(models.Pages)