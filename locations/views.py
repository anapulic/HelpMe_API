from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import KorisnikUOpasnosti
from .serializers import KorisnikUOpasnostiSerializer
from django.http import Http404


#Ispisi sve ili stvori novo u JSON formatu
#localhost:8000/korisnik
class KorisnikUOpasnostiList(APIView):

    def get(self, request):
        korisnikUOpasnosti = KorisnikUOpasnosti.objects.all()
        serializer = KorisnikUOpasnostiSerializer(korisnikUOpasnosti, many=True)
        return Response(serializer.data)


#Dodaj novog korisnika u JSON formatu
#localhost:8000/korisnik/new
class NoviKorisnikUOpasnosti (APIView):
    
    def post(self, request):
        serializer = KorisnikUOpasnostiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Dohvaćanje i ažuriranje postojećih korisnika
#localhost:8000/korisnik/<id>
class KorisnikUOpasnostiDetails (APIView):

    def get_object(self, pk):
        try:
            return KorisnikUOpasnosti.objects.get(pk=pk)
        except KorisnikUOpasnosti.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = KorisnikUOpasnostiSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = KorisnikUOpasnostiSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
