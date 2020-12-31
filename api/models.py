from django.db import models


class Organizer(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=9)
    description = models.CharField(max_length=300)


class Event(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    localization = models.CharField(max_length=32)
    description = models.CharField(max_length=200)
    judge_qr = models.CharField(max_length=16)


class Competition(models.Model):
    COMPETITION_TYPES = (
        ('R', 'race'),
        ('T', 'timerace'),
        ('P', 'physical'),
        ('K', 'knowledge'),
    )

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=COMPETITION_TYPES)


class Crew(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET(0))
    number = models.IntegerField()
    car = models.CharField(max_length=64)
    year_of_production = models.CharField(max_length=4)
    driver_name = models.CharField(max_length=32)
    qr = models.CharField(max_length=16)
    photo = models.ImageField(upload_to='images', blank=True)
    description = models.CharField(max_length=200)


class Score(models.Model):
    COMPETITION_TYPES = (
        ('R', 'race'),
        ('T', 'timerace'),
        ('P', 'physical'),
        ('K', 'knowledge'),
    )
    competition = models.CharField(max_length=1, choices=COMPETITION_TYPES)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    score = models.CharField(max_length=32)
    date = models.DateField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
