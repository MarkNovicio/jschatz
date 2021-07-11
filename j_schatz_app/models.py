from django.db import models

# Create your models here.

class UserMessageManager(models.Manager):
    def basic_validator(self, post_data):
        errors={}

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        if len(post_data['username']) < 2:
            errors['username'] = "Username must have at least 2 characters"

        if len(post_data['message']):
            errors['message'] = "Message should be at least 10 characters"
        
        return errors
        
class UserMessage(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserMessageManager()

    def __repr__(self):
        return f'Name: {self.name} | email: {self.email} | message: {self.message}'


    
