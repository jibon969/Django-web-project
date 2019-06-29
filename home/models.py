from django.db import models

# Create your models here.


# Features Models
class Feature(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']


# Portfolio Models
class Portfolio(models.Model):
    image = models.ImageField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-updated_on']


# Comment Models
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name







