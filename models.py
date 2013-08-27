from django.db import models

# Create your models here.
class Site(models.Model):
    tag = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    def __str__(self):
        return self.tag
    def __unicode__(self):
        return self.tag
