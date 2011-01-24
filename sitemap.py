from datetime import datetime
from django.contrib.sitemaps import Sitemap
from basic.blog.models import Post
from vendors.models import Vendor
from schedule.models import Event

class CFMSitemap(Sitemap):
    changefreq="always"
    priority=0.5
    
    def items(self):
        return Post.objects.filter(publish__gte=datetime.now())
    
    def lastmod(self, obj):
        return obj.publish
