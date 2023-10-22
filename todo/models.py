from django.db import models
from django.urls import reverse

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(unique=True)
    completed = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    
    def __Str__(self):
        return self.title