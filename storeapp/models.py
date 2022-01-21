from enum import Enum

from django.db import models


class Book(models.Model):
    class BookType(Enum):
        UNDEFINED = 'Undefined'
        ADVENTURE = 'Adventure'
        BIOGRAPHY = 'Biography'
        DYSTOPIA = 'Dystopia'
        FANTASTIC = 'Fantastic'
        HORROR = 'Horror'
        SCIENCE = 'Science'
        SCIENCE_FICTION = 'ScienceFiction'
        POETRY = 'Poetry'

    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publishedData = models.DateField()
    background = models.TextField()
    price = models.FloatField()
    poster = models.TextField()
    category = BookType.UNDEFINED
    objects = models.QuerySet()
