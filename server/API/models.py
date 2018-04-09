from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    img = models.ImageField()

    def __str__(self):
        return str(self.name)

class Image(models.Model):
    actor = models.ForeignKey(Actor)
    img = models.ImageField()

    def __str__(self):
        return str(self.actor)


class Carrer(models.Model):
    actor = models.ForeignKey(Actor)
    year = models.CharField(max_length=4)
    content = models.TextField()

    def __str__(self):
        return str(self.actor)


class Video(models.Model):
    actor = models.ForeignKey(Actor)
    video = models.CharField(max_length=45)

    def __str__(self):
        return str(self.actor)