import math
from .bitola import *

def calculos_avancada(data):
    # diametro_econ = 0
    data['potencia'] = data['desnivel']*data['vazao']*9.81*0.531
    diametro_econ = 123.7*(((float(data['vazao'])/1000)**3)/(1.2*float(data['desnivel'])))**(1/7)*10
    tubos_comerciais = [75,100,125,150,200,250,300,350,400,450,500,550,600,650,700,750,800]
    tubos_comerciais.sort()
    diametro_comercial = math.ceil(diametro_econ)
    
    for i in tubos_comerciais:
        if diametro_comercial < i:
            diametro_comercial = i
            break
            
    vel_escoamento = (4*float(data['vazao'])/1000)/((math.pi)*((diametro_comercial/1000)**2))
    perda_carga_unit = (vel_escoamento/(0.355*140*(diametro_comercial/1000)**0.63))**(1/0.54)
    perda_carga_tub = perda_carga_unit*data['dist_hidr']
    k = 3.6
    perda_carga_conex_total = k*(vel_escoamento**2)/(2*9.81)

    if perda_carga_tub + perda_carga_conex_total <= data['desnivel']:
        perda_carga_total = perda_carga_tub + perda_carga_conex_total

    desnivel_real = data['desnivel'] - perda_carga_total
    porcentagem_perda = (perda_carga_total / data['desnivel'])
    potencia = data['vazao']*desnivel_real*9.81*0.64
    mchs = potencia/1000

    if potencia%1000 >= 500:
        mchs = math.ceil(mchs)
    else:
        mchs = math.floor(mchs)

    if data['modelo'] == 'On':
        tensao = 220.0
    else:
        tensao = 130.0

    if data['modelo'] == 'On':
        corrente = potencia/tensao
    else:
        corrente = potencia/tensao/math.sqrt(3)


    if data['tipo_cabo'] == 'A':
        ro = 0.0282
    else:
        ro = 0.0172

    for i in bitola:
        f_pot = 1.0
        perda_porc = 1.0
        r = (ro*data['dist_eletr'])/i
        delta_e = 2*r*corrente*f_pot
        perda_porc = delta_e/tensao

        if perda_porc <= 0.05 and corrente<=bitola[i]:
            bitola_real = i
            pot_util = potencia*(1-perda_porc)
            break
    dados = {
            'diametro_econ':diametro_econ,
            'diametro_comercial':diametro_comercial,
            'vel_escoamento':vel_escoamento,
            'perda_carga_unit':perda_carga_unit,
            'perda_carga_tub':perda_carga_tub,
            'perda_carga_conex_total':perda_carga_conex_total,
            'desnivel_real':desnivel_real,
            'porcentagem_perda':"{0:.0%}".format(porcentagem_perda),
            'pot_util':pot_util,
            'mchs':mchs,
            'bitola_real':bitola_real,        
        }
    return dados