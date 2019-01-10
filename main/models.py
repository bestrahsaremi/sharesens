from django.db import models
from datetime import datetime

class Sentences(models.Model):
    title = models.CharField(max_length=80, blank=False)
    description = models.CharField(max_length=400, blank=False, default="some description")
    image = models.ImageField(upload_to="images", blank=False, default="default.png")
    created_at=models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return self.title