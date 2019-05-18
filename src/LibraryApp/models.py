from django.db import models

class Book(models.Model):
    title = models.CharField("book's title", max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s | %s" % (self.title, self.author)

class Author(models.Model):
    first_name = models.CharField("author's first name", max_length=50)
    last_name = models.CharField("author's last name",max_length=50)
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)