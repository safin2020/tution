from django.db import models

# Create your models here.
# admin control model

# joining class model
class JoiningClass(models.Model):
    joiningText = models.TextField(blank=True)
    noclasstext = models.TextField(blank=True)
    classlink = models.URLField(max_length=200,blank=True)
    noticeText = models.TextField(blank=True,null=True)
    active = models.BooleanField(default=False)
