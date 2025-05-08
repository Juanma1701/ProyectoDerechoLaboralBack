from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=50)
    last = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=254,blank=False,null=True)
    
    def __str__(self):
        return self.name
    

class Leyes(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=254)

    def __str__(self):
        return self.name

