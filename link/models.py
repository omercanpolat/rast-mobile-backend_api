from django.db import models

# Create your models here.
class Link(models.Model):
  link = models.CharField(max_length=64)
  link_name = models.CharField(max_length=64)
  description = models.TextField()
  
  def __str__(self):
    return self.link_name
