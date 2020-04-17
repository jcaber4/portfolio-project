from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=300)
