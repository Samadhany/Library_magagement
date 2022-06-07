from sre_parse import State
from django.db import models

NO_COPIES = (
    ('1','1000'),
    ('2', '2000'),
    ('3','3000'),
)


# Create your models here.
class User(models.Model):
 Book_Name = models.CharField(max_length=40)
 title = models.CharField(max_length=40)
 author = models.CharField(max_length=40)
 summary = models.CharField(max_length=40)
 language = models.CharField(max_length=40)
 total_copies = models.CharField(max_length=40)
 available_copies = models.CharField(max_length=6, choices=NO_COPIES, default='abc')
