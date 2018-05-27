from rest_framework import serializers
from .models import KorisnikUOpasnosti


class KorisnikUOpasnostiSerializer(serializers.ModelSerializer):

    class Meta:
        model = KorisnikUOpasnosti
        fields = '__all__'

