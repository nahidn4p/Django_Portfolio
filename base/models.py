from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.email}"