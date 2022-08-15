from rest_framework import serializers
from calculadoras.models import LeadBasica, LeadAvancada
from calculadoras.calculos import calculos_avancada
import math

class LeadBasicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeadBasica
        fields = '__all__'
        read_only_fields = ['potencia','mchs']
    
    def create(self,data):
        data['potencia'] = math.ceil(data['desnivel']*data['vazao']*9.81*0.531)
        if data['potencia'] <= 75000:
            data['mchs'] = data['potencia']/1000
            if data['potencia']%1000 >= 500:
                data['mchs'] = math.ceil(data['mchs'])
            else:
                data['mchs'] = math.floor(data['mchs'])
        else:
            data['potencia'] = 75000
            data['mchs'] = 75
        return LeadBasica.objects.create(**data)
        

class LeadAvancadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeadAvancada
        fields = '__all__'
        read_only_fields = [
            'potencia','mchs','diametro_econ','diametro_comercial','vel_escoamento',
            'perda_carga_unit','perda_carga_tub','perda_carga_conex_total','desnivel_real',
            'porcentagem_perda','bitola_real'
        ]

    def create(self, data):
        contas = calculos_avancada(data)
        data['potencia'] = contas['pot_util']
        data['mchs'] = contas['mchs']
        data['bitola_real'] = contas['bitola_real']
        data['diametro_econ'] = contas['diametro_econ']
        data['diametro_comercial'] = contas['diametro_comercial']
        data['vel_escoamento']= contas['vel_escoamento']
        data['perda_carga_unit'] = contas['perda_carga_unit']
        data['perda_carga_tub'] = contas['perda_carga_tub']
        data['perda_carga_conex_total'] = contas['perda_carga_conex_total']
        data['desnivel_real'] = contas['desnivel_real']
        data['porcentagem_perda'] = contas['porcentagem_perda']
        return LeadAvancada.objects.create(**data)
    
