from django.db import models

class UserManager(models.Manager):
    def validator(self, post_data):
        
        errors = {}
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters long"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters long"
        if len(post_data['password']) < 8:
            errors['password'] = "Password should be at least 8 charcters long"
        if post_data['password'] != post_data['confirm_password']:
            errors['password'] = "Password does not match"


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

