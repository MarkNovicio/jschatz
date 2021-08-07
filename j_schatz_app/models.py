from django.db import models
from login_app.models import User
import re
# Create your models here.

class UserMessageManager(models.Manager):
    def basic_validator(self, post_data):
        errors={}

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        if len(post_data['username']) < 2:
            errors['username'] = "Username must have at least 2 characters"

        if len(post_data['message']) < 10:
            errors['message'] = "Message should be at least 10 characters"
        
        return errors

class CodeChallengeManager(models.Manager):
    def basic_validator(self, post_data):
        errors={}

        if len(post_data['title']) < 1:
            errors['username'] = "Please enter title"

        if len(post_data['challenge_question']) < 5:
            errors['message'] = "Please enter a challenge question"
        
        return errors

class UserMessage(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserMessageManager()

    def __repr__(self):
        return f'Name: {self.username} | email: {self.email} | message: {self.message}'

class CodeChallenge(models.Model):
    title = models.CharField(max_length = 50)
    challenge_question = models.TextField()
    creator = models.ForeignKey(User, related_name = 'code_challenges', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CodeChallengeManager()

    def __repr__(self):
        return f'Title: {self.title} | Challenge Question: {self.challenge_question}'

