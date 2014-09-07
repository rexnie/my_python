from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name;
