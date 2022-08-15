from rest_framework import viewsets, status
from calculadoras.models import LeadBasica, LeadAvancada
from calculadoras.serializers import LeadBasicaSerializer, LeadAvancadaSerializer
from rest_framework.response import Response


class LeadBasicaViewSet(viewsets.ModelViewSet):
    """Exibe todos os Leads da Calculadora Básica"""
    queryset = LeadBasica.objects.all()
    serializer_class = LeadBasicaSerializer
    http_method_names = ['get','post',]

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri()+id
            return response

class LeadAvancadaViewSet(viewsets.ModelViewSet):
    """Exibe todos os leads da Calculadora Avançada"""
    queryset = LeadAvancada.objects.all()
    serializer_class = LeadAvancadaSerializer
    http_method_names = ['get','post']

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri()+id
            return response
    