from django.contrib.sitemaps import Sitemap

from .models import Post


def _last_model(obj):
    return obj.updated_on


class PostSitemap(Sitemap):
    change_frequency = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.filter(status=1)

    # def location(self, item):
    #     return reverse(item)
