from django.db import models

MODELOS = (
        ('On', 'On Grid'),
        ('Off','Off Grid')
    )
CABOS =(
    ('A','Alumínio'),
    ('C','Cobre')
)
class LeadBasica(models.Model):
    nome = models.CharField(max_length = 50, blank = False, null=False)
    telefone = models.CharField(max_length = 20, blank = True, null=True)
    email = models.EmailField(max_length = 50, blank = False, null=False)
    concessionaria = models.CharField(max_length = 50,  blank = True, null=True)
    desnivel = models.IntegerField(blank = False, null=False)
    vazao = models.IntegerField(blank = False, null=False)
    modelo = models.CharField(max_length = 10, blank = False, null=False,choices=MODELOS,default='On')
    potencia = models.IntegerField(blank = False, null=False, default=0)
    mchs = models.IntegerField(blank = False, null=False, default=0)
    data = models.DateField(blank = False, null=False)

    def __str__(self):
        return self.nome

class LeadAvancada(models.Model):
    nome = models.CharField(max_length = 50, blank = False, null=False)
    telefone = models.CharField(max_length = 20,blank = True, null=True)
    email = models.CharField(max_length = 50, blank = False, null=False)
    concessionaria = models.CharField(max_length = 50,blank = True, null=True)
    desnivel = models.IntegerField(blank = False, null=False)
    vazao = models.IntegerField(blank = False, null=False)
    dist_hidr = models.IntegerField(blank = False, null=False)
    dist_eletr = models.IntegerField(blank = False, null=False)
    modelo = models.CharField(max_length = 10, blank = False, null=False,choices=MODELOS,default='On')
    tipo_cabo = models.CharField(max_length =10,  blank = False, null=False,choices=CABOS,default='A')
    potencia = models.IntegerField(blank = False, null=False)
    mchs = models.IntegerField(blank = False, null=False)
    data = models.DateField(blank = False, null=False)
    diametro_econ = models.FloatField(blank = False, null=False)
    diametro_comercial = models.IntegerField(blank = False, null=False)
    vel_escoamento = models.FloatField(blank = False, null=False)
    perda_carga_unit = models.FloatField(blank = False, null=False)
    perda_carga_tub = models.FloatField(blank = False, null=False)
    perda_carga_conex_total = models.FloatField(blank = False, null=False)
    desnivel_real = models.FloatField(blank = False, null=False)
    porcentagem_perda = models.CharField(max_length=10, blank = False, null=False)
    bitola_real = models.IntegerField(blank = False, null=False)

    def __str__(self):
        return self.nome
