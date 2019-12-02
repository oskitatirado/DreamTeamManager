'''
Created on 24 oct. 2019

@author: robet_000
'''
from django import template

from main.models import Usuario,Puja,Jugador,User, Alineacion

register = template.Library()


@register.assignment_tag
def get_venta(valor,nombre):
    print("entro en get venta")
    user=User.objects.get(username=nombre)
    usuario=Usuario.objects.get(user=user)
    jugador=Jugador.objects.get(idJugador=valor)
    try:
        puja=Puja.objects.get(estadoPuja='P',pujador=usuario,jugadores=jugador)
        print(puja)
    except:
       
        return False
   
    return True
@register.simple_tag
def get_oferta(valor,nombre): 
    print("Entro en getOferta")
    user=User.objects.get(username=nombre)
    usuario=Usuario.objects.get(user=user)
    jugador=Jugador.objects.get(idJugador=valor) 
    try:
        puja=Puja.objects.get(estadoPuja='P',pujador=usuario,jugadores=jugador)
       
    except:
        return ""
   
    return puja.valor
    
@register.simple_tag
def get_posicion(nombre): 
    print("Entro en getPosicion")
    if nombre=='B':
        return 'Base'
    elif nombre== 'E':
        return 'Escolta'
    elif nombre == 'A':
        return 'Alero'
    elif nombre== 'AP':
        return 'Ala-pivot'
    elif nombre== 'P':
        return 'Pivot'
    elif nombre== 'E-A' or nombre == 'A-E':
        return 'Escolta-Alero'
    else:
        return 'Error'
    