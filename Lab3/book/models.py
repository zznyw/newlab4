#encoding:utf-8
from django.db import models

# Create your models here.
        
class Author(models.Model):
    AuthorID = models.CharField(max_length=15, primary_key=True)
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=15)
    Country = models.CharField(max_length=50)
    def __unicode__(self):
        return self.Name
        
class Book(models.Model):
    ISBN = models.CharField(max_length=15, primary_key=True)
    Title = models.CharField(max_length=100)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=30)
    PublishDate = models.CharField(max_length=50)
    Price = models.CharField(max_length=15)

    def __unicode__(self):
        return self.Title