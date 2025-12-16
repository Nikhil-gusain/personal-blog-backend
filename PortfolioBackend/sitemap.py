from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from portfolioApi.models import Blogs, Skills

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Blogs.objects.all().order_by('-createdAt')

    def lastmod(self, obj):
        return obj.createdAt
    
    def location(self,obj):
        return reverse('blogDetailPage', args=[obj.slug])

class TagSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = 'https'

    def items(self):
        return Skills.objects.all()

    def location(self, obj):
        return reverse('blogbytag', args=[obj.name])

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return ['blogPage']

    def location(self, item):
        return reverse(item)
