from django.db import models
from django.contrib.auth.models import User
from configuration.models import Score

# Create your models here.
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    document = models.IntegerField()
    document_type = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'user: {self.user_name} | {self.id}'
    
class UserQualification(models.Model):
    id = models.AutoField(primary_key=True)
    user_from = models.ForeignKey(User)
    user_to = models.ForeignKey(User)
    score = models.ForeignKey(Score)

    def __str__(self):
        return f'{self.user_from} rated {self.user_to} = {self.score}'