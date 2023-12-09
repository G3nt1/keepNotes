from django.db import models


# Create your models here.
class BigNotes(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title
