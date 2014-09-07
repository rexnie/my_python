from django.db import models

sex_choices = (
    ('f', 'female'),
    ('m', 'male'),
)

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 30)
    sex = models.CharField(max_length = 1, choices = sex_choices)

    def __unicode__(self):
        return self.name
