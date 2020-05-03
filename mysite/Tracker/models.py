from django.db import models

class Squirrel(models.Model):

    def __str__(self):
        return self.unique_squirrel_id
    
    unique_squirrel_id = models.CharField(
	'ID',
        max_length = 100,
        unique = True,
        primary_key = True,
    )

    date = models.DateTimeField('Date',)
# Create your models here.
