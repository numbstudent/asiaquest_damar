from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    label = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.label

class Books(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.BigIntegerField()
    stock = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    keywords = models.CharField(max_length=50)
    categories = models.ManyToManyField(Categories)



