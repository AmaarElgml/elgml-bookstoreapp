from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    image = models.TextField()
    booksNum = models.IntegerField()
    objects = models.QuerySet()


class Book(models.Model):
    class BookType(models.TextChoices):
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
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)
    background = models.TextField()
    price = models.FloatField()
    poster = models.TextField()
    category = models.CharField(max_length=50, choices=BookType.choices, default=BookType.UNDEFINED)
    objects = models.QuerySet()


class News(models.Model):
    class NewsType(models.TextChoices):
        UNDEFINED = 'Undefined'
        COMPLETED = 'Completed'
        KNOWLEDGE = 'Knowledge'
        GOOD = 'Good'
        BAD = 'Bad'

    title = models.TextField()
    body = models.TextField()
    date = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=NewsType.choices, default=NewsType.UNDEFINED)
    objects = models.QuerySet()


class AppAdmin(models.Model):
    class AppAdminRole(models.TextChoices):
        UNDEFINED = 'Undefined'
        ADMIN = 'Admin'
        MODERATOR = 'Moderator'
        EDITOR = 'Editor'
        ANALYST = 'Analyst'

    name = models.CharField(max_length=50)
    image = models.TextField()
    role = models.CharField(max_length=50, choices=AppAdminRole.choices, default=AppAdminRole.UNDEFINED)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    online = models.BooleanField()
    objects = models.QuerySet()
