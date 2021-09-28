from django.db import models
from picklefield.fields import PickledObjectField


class Author(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    writer = models.ForeignKey('Author', on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
