from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    thumbs = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.sub_title

    full_name.admin_order_field = 'title'
