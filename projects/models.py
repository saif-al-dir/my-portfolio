# projects/models.py
from django.db import models
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    link = models.URLField(max_length=500, blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True) # Requires Pillow: pip install Pillow

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})