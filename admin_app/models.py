from django.db import models

class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.description}"

class Price(models.Model):
    range = models.ValueRange()

    def __str__(self):
        return f"{self.range} "
