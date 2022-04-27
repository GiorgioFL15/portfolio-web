from django.db import models

class Form(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=13)
    site= models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

