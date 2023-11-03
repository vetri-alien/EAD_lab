from django.db import models

# Create your models here.
class Data(models.Model):
    book_name = models.CharField(max_length=100)
    book_number = models.IntegerField()

    def __str__(self):
        return str(self.book_name)
