from django.shortcuts import render
from rest_framework import generics

from .serializers import SatelliteSerializer
from .models import Satellite

# Create your views here.

def renderUI(request):
    return render(request, 'satellite/index.html')
    
class SatelliteListAPI(generics.ListAPIView):
    serializer_class = SatelliteSerializer
    queryset = Satellite.objects.all()

class SatelliteCreateAPI(generics.CreateAPIView):
    serializer_class = SatelliteSerializer