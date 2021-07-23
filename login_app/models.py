from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors={}
       # today = datetime.today()
        email_check = self.filter(email=post_data['email'])
        if email_check:
            errors['email'] = "Email already in use" 
            #compares user email input to what is in database

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name must have at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name must have at least 2 characters"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must contain 8 characters"
        if len(post_data['password']) < 0:
            errors['password'] = "Password must contain 8 characters"
        if post_data['confirm_pw'] != post_data['password']:
            errors['confirm_pw'] = "Confirm Password must match Password"
        return errors
    

class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100, unique = True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
    def __repr__(self):
        return f'Name: {self.first_name} | email: {self.last_name} | message: {self.email}'

