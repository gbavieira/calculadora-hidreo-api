from rest_framework import viewsets
from calculadoras.models import LeadBasica, LeadAvancada
from calculadoras.serializers import LeadBasicaSerializer, LeadAvancadaSerializer
from rest_framework.response import Response


class LeadBasicaViewSet(viewsets.ModelViewSet):
    """Exibe todos os Leads da Calculadora Básica"""
    queryset = LeadBasica.objects.all()
    serializer_class = LeadBasicaSerializer
    http_method_names = ['get','post',]

class LeadAvancadaViewSet(viewsets.ModelViewSet):
    """Exibe todos os leads da Calculadora Avançada"""
    queryset = LeadAvancada.objects.all()
    serializer_class = LeadAvancadaSerializer
    http_method_names = ['get','post']
    