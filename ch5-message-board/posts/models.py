from django.db import models


# Create your models here.
class Post(models.Model):
    text = models.TextField()

    # Show database entry in human readable format
    def __str__(self):
        return self.text[:50]
