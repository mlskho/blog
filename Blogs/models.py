from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blogpost(models.Model):
    """Blogpost"""
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
   

    def __str__(self):
        """Return  string representation of the title."""
        return self.title

    def __str__(self):
        '''Return a string representation of the model.'''    
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text

        
