from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        """A string representation of the model."""
        return self.name

