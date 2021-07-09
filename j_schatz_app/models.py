from django.db import models

# Create your models here.

class UserMessage(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=3000)

    def __repr__(self):
        return f'Name: {self.name} | email: {self.email} | message: {self.message}'


    
