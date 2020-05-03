from django.db import models

class Squirrel(models.Model):

    def __str__(self):
        return self.unique_squirrel_id
    
    unique_squirrel_id = models.CharField(
	'ID',
        max_length = 100,
        #help_text = _('Unique Squirrel ID'),
        unique = True,
        primary_key = True,
    )

    date = models.DateTimeField(
	'Date',
        #help_text = _('Date'),
        null = True,
    )
# Create your models here.
