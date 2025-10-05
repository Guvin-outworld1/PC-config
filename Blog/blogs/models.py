"""
管理整个项目模型
"""

from django.db import models


class Blogger(models.Model):
    """博主"""

    name = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BlogArticle(models.Model):
    """博文"""

    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.text) <= 50:
            return self.text

        return self.text[:50] + "..."
