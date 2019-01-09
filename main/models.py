from django.db import models

class Sentences(models.Model):
    title = models.CharField(max_length=120, blank=False)

    def __str__(self):
        return self.title