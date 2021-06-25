from django.db import models

class City(models.Model):
    name = models.CharField(max_length=128, verbose_name='')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name
