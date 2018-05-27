from django.db import models


class KorisnikUOpasnosti(models.Model):
    ime = models.CharField(max_length=25)
    prezime = models.CharField(max_length=35)
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.ime