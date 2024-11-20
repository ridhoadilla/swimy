from django.db import models

class Pool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pools/', blank=True, null=True)

    def __str__(self):
        return self.name
