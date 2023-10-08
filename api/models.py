from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Perfume(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def __str__(self):
        return self.title


class Rating(models.Model):
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    # def __str__(self):
    #      return self.perfume


    class Meta:
        unique_together = (('user', 'perfume'),)
        index_together = (('user', 'perfume'),)