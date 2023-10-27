from django.db import models


# Create your models here.
class Cars(models.Model):
    CAR_FOR_CHOICE = (
        ('E', 'Electric car'),
        ('N', 'Gas car')
    )
    name = models.CharField(max_length=50)
    car_type = models.CharField(choices=CAR_FOR_CHOICE, max_length=2)

    def __str__(self):
        return self.name
