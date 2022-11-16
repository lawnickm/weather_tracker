from django.shortcuts import render
from rest_framework import generics

from .serializers import SatelliteSerializer
from .models import Satellite

# Create your views here.

def renderUI(request):
    return render(request, 'satellite/index.html')
    
# satellite/list
class SatelliteListAPI(generics.ListAPIView):
    serializer_class = SatelliteSerializer
    queryset = Satellite.objects.all()

# satellite/create
class SatelliteCreateAPI(generics.CreateAPIView):
    serializer_class = SatelliteSerializer