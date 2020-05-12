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
    
    latitude = models.FloatField('latitude', max_length = 20, null = True)

    longitude = models.FloatField('longitude', max_length = 20, null = True)

    shift_choices = (
        ('AM', 'AM'),
        ('PM', 'PM'),
    )

    shift = models.CharField(
            'shift',
            max_length = 2,
            choices = shift_choices,
            default = 'AM',
    )

    date = models.DateTimeField('Date', null = True)

    age = models.CharField('Age', max_length = 10, null = True)

    primary_fur_color = models.CharField('Primary Fur Color', max_length = 100, null = True)

    specific_location = models.CharField('Specific Location', max_length = 100, null = True)

    TF_choices = (
        ('true', 'True'),
        ('false', 'False'),
        ('', ''),
    )

    running = models.CharField(
            'running',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )

    chasing = models.CharField(
            'chasing',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )

    climbing = models.CharField(
            'climbing',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )

    eating = models.CharField(
            'eating',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )

    foraging = models.CharField(
            'foraging',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )

    other_activities = models.CharField('other activities', max_length = 100, null = True)

    kuks = models.CharField(
            'kuks',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )

    quaas = models.CharField(
            'quaas',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )

    moans = models.CharField(
            'moans',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )

    tail_flags = models.CharField(
            'tail flags',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )

    tail_twitches = models.CharField(
            'tail twitches',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )

    approaches = models.CharField(
            'approaches',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )

    indifferent = models.CharField(
            'indifferent',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )

    runs_from = models.CharField(
            'runs_from',
            max_length = 10,
            choices = TF_choices,
            default = '',
    )
