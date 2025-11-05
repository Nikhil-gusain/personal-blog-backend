# myapp/models.py

from mongoengine import (
    Document,
    StringField,
    IntField,
    URLField,
    DictField,
    ListField,
    ReferenceField,
    DateTimeField,
    CASCADE,
)
from PortfolioBackend.Utils import Helpers
import datetime


# ─────────────────────────────
# Pages
# ─────────────────────────────
class Pages(Document):
    name = StringField(max_length=200, required=True)

    def __str__(self):
        return self.name


# ─────────────────────────────
# About Section
# ─────────────────────────────
class About(Document):
    sectionTitle = StringField(max_length=200)
    name = StringField(max_length=100)
    designation = StringField()
    bio = StringField()
    profileImage = URLField(max_length=2500)
    details = DictField(default=dict)
    cvLink = URLField(max_length=2500)


# ─────────────────────────────
# Skills
# ─────────────────────────────
class Skills(Document):
    name = StringField(max_length=200, required=True)
    percent = IntField()


# ─────────────────────────────
# Blogs
# ─────────────────────────────
class Blogs(Document):
    title = StringField(max_length=200)
    excerpt = StringField()
    coverImage = URLField(max_length=2500)
    content = StringField()  # you can replace with QuillField if integrated
    readMin = IntField(default=0)
    category = ReferenceField(Skills, reverse_delete_rule=CASCADE, null=True)
    createdAt = DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Calculate reading time using your helper
        try:
            self.readMin = Helpers.CalculateReadingTime(self.content)
        except Exception:
            pass
        return super().save(*args, **kwargs)


# ─────────────────────────────
# SkillSection
# ─────────────────────────────
class SkillSection(Document):
    sectionTitle = StringField(max_length=200)
    intro = StringField()
    # Store related skill IDs in a list
    skills = ListField(ReferenceField(Skills))

    def __str__(self):
        return self.sectionTitle


# ─────────────────────────────
# Services
# ─────────────────────────────
class Services(Document):
    title = StringField(max_length=200)
    description = StringField()
    icon = URLField(max_length=2500)
    # Store Django User reference or your custom User model if migrated
    author = StringField(max_length=200, default="Admin")
    createdAt = DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.title


# ─────────────────────────────
# ServiceSection
# ─────────────────────────────
class ServiceSection(Document):
    title = StringField(
        max_length=200,
        help_text="What I <span class='text-yellow-500'>Provide</span> Add span tag with tailwind to highlight",
    )
    subtitle = StringField(max_length=200)
    services = ListField(ReferenceField(Services))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.subtitle:
            self.subtitle = self.subtitle.upper()
        return super().save(*args, **kwargs)


# ─────────────────────────────
# Social Links
# ─────────────────────────────
class SocialLinks(Document):
    icon = StringField(max_length=200)
    url = URLField(max_length=2500)

    def __str__(self):
        return self.icon


# ─────────────────────────────
# HeroSection
# ─────────────────────────────
class HeroSection(Document):
    page = ReferenceField(Pages, reverse_delete_rule=CASCADE, null=True)
    title = StringField(max_length=200)
    highlight = StringField(max_length=200)
    subtitle = StringField()
    socialLinks = ListField(ReferenceField(SocialLinks))

    def __str__(self):
        return f"{self.page.name if self.page else 'Unknown Page'} - Hero Section"


# ─────────────────────────────
# ContactSection
# ─────────────────────────────
class ContactSection(Document):
    title = StringField(max_length=200)
    info = DictField(
        default=dict,
        help_text="""
        [
            {
                "label": "Address",
                "value": "New Delhi, Delhi, India",
                "icon": "map-pin"
            }
        ]
        """,
    )
    socialLinks = ListField(ReferenceField(SocialLinks))

    def __str__(self):
        return self.title


# ─────────────────────────────
# Blog (second type)
# ─────────────────────────────
class Blog(Document):
    title = StringField(max_length=200)
    excerpt = StringField()
    coverImage = URLField(max_length=2500)
    content = StringField(max_length=2500)
    tag = StringField(max_length=200)
    category = ReferenceField(Skills, reverse_delete_rule=CASCADE, null=True)
    createdAt = DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.title
