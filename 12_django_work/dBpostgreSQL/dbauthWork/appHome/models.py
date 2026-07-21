from django.db import models
from django.contrib.auth.models import User 

class todoData(models.Model):
    # Django creates 'id SERIAL PRIMARY KEY' automatically here behind the scenes
    # Links to auth_user table id
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Your updated To-Do fields
    title = models.CharField(max_length=250 , null=False , blank= False)
    description = models.TextField(blank=True, null=True) # Allows description to be optional
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Displays the creator's username and the task title in Django Admin
        return f"{self.user.username} - {self.title}"
