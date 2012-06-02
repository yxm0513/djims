from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    category_id = models.ForeignKey('Category')
    description = models.TextField()
    create_at = models.TimeField()

    def __unicode__(self):
        return self.name;

    def __str__(self):
        return self.name;


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __unicode__(self):
        return self.name;

