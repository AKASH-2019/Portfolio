from django.db import models

# Create your models here.

class Project(models.Model):
  title = models.CharField(max_length=200)
  image = models.ImageField(blank=True, null=True, upload_to='project')
  description = models.TextField()
  completed = models.BooleanField(default=False, blank=True, null=True)
  github = models.URLField(blank=True)
  web = models.URLField(blank=True)
  
      
  def __str__(self):
    return self.title