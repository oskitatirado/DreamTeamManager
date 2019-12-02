'''
Created on 8 oct. 2019

@author: robet_000
'''
from main.models import *
from random import randrange
from test.test_argparse import bases


def prueba_task():
    liga=Liga.objects.all()
    jugadores=Jugador.objects.filter(liga=liga[0])
    n=randrange(len(jugadores))
    j=jugadores[n]
    print(j)
    j.valor=1996
    j.save()

def actualizar_puntuacion():
    print('Entro en actualizar puntuacion')
    jugadores=Usuario.objects.all().exclude(user__username__contains='Agente')
    
    for j in jugadores:
        alineaciones=Alineacion.objects.filter(usuarios=j,tipoAlineacion='D').order_by('-fechaAlineacion')
        alineacion=alineaciones[0]
        if alineacion.orden is None:
            alineacion.puntuacion=-40
            alineacion.save()
        else:
            players=alineacion.orden.split('#')
            base=players[0]
            escolta=players[1]
            alero=players[2]
            ap=players[3]
            pivot=players[4]
            bs=players[5]
            es=players[6]
            alers=players[7]
            aps=players[8]
            ps=players[9]
            if not base == 'NULL':
                jug=Jugador.objects.get(idJugador=base)
                alineacion.puntuacion+=jug.puntuacion+(jug.puntuacion*0.5)
                alineacion.save()
            else:
                alineacion.puntuacion+=-4
                alineacion.save()
            if not escolta == 'NULL':
                jug=Jugador.objects.get(idJugador=escolta)
                alineacion.puntuacion+=jug.puntuacion+(jug.puntuacion*0.5)
                alineacion.save()
            else:
                alineacion.puntuacion+=-4
                alineacion.save()
            if not alero == 'NULL':
                jug=Jugador.objects.get(idJugador=alero)
                alineacion.puntuacion+=jug.puntuacion+(jug.puntuacion*0.5)
                alineacion.save()
            else:
                alineacion.puntuacion+=-4
                alineacion.save()
            if not ap == 'NULL':
                jug=Jugador.objects.get(idJugador=ap)
                alineacion.puntuacion+=jug.puntuacion+(jug.puntuacion*0.5)
                alineacion.save()
            else:
                alineacion.puntuacion+=-4
                alineacion.save()
            if not pivot == 'NULL':
                jug=Jugador.objects.get(idJugador=pivot)
                alineacion.puntuacion+=jug.puntuacion+(jug.puntuacion*0.5)
                alineacion.save()
            else:
                alineacion.puntuacion+=-4
                alineacion.save()
            if not bs == 'NULL':
                jug=Jugador.objects.get(idJugador=bs)
                alineacion.puntuacion+=jug.puntuacion
                alineacion.save()
            else:
                alineacion.puntuacion+=-4
                alineacion.save()
            if not es == 'NULL':
                jug=Jugador.objects.get(idJugador=es)
                alineacion.puntuacion+=jug.puntuacion
                alineacion.save()
            else:
                alineacion.puntuacion+=-4
                alineacion.save()
            if not alers == 'NULL':
                jug=Jugador.objects.get(idJugador=alers)
                alineacion.puntuacion+=jug.puntuacion
                alineacion.save()
            else:
                alineacion.puntuacion+=-4
                alineacion.save()
            if not aps == 'NULL':
                jug=Jugador.objects.get(idJugador=aps)
                alineacion.puntuacion+=jug.puntuacion
                alineacion.save()
            else:
                alineacion.puntuacion+=-4
                alineacion.save()
            if not ps == 'NULL':
                jug=Jugador.objects.get(idJugador=ps)
                alineacion.puntuacion+=jug.puntuacion
                alineacion.save()
            else:
                alineacion.puntuacion+=-4
                alineacion.save()
            
        


def azar():
    opc=[-2,2,6,10,13]
    n=randrange(len(opc))
    return opc[n]


def crearMercado(liga):
    
    agente=Usuario.objects.get(user__username__contains='Agente',liga=liga)
    agentes=Jugador.objects.filter(usuarios=agente,mercado=False)
    bases=agentes.filter(posicion="B")
    escoltas=agentes.filter(posicion__contains="E")
    aler=agentes.filter(posicion__contains="A")
    aleros=aler.exclude(posicion="AP")
    alapivots=agentes.filter(posicion="AP")
    pivots=agentes.filter(posicion="P")
    addB=bucle(bases,6)
    addE=bucle(escoltas,6)
    addA=bucle(aleros,6)
    addAP=bucle(alapivots,6)
    addP=bucle(pivots,6)
    for j in addB:
        Jugador.objects.filter(idJugador=j.idJugador).update(mercado=True)
    for j in addE:
        Jugador.objects.filter(idJugador=j.idJugador).update(mercado=True)
    for j in addA:
        Jugador.objects.filter(idJugador=j.idJugador).update(mercado=True)
    for j in addAP:
        Jugador.objects.filter(idJugador=j.idJugador).update(mercado=True)
    for j in addP:
        Jugador.objects.filter(idJugador=j.idJugador).update(mercado=True)    



def add_jugadores(usuario,liga):
    agente=Usuario.objects.get(user__username__contains='Agente',liga=liga)
    agentes=Jugador.objects.filter(usuarios=agente)
    bases=agentes.filter(posicion="B")
    escoltas=agentes.filter(posicion__contains="E")
    aler=agentes.filter(posicion__contains="A")
    aleros=aler.exclude(posicion="AP")
    alapivots=agentes.filter(posicion="AP")
    pivots=agentes.filter(posicion="P")
    addB=bucle(bases,5)
    addE=bucle(escoltas,3)
    addA=bucle(aleros,5)
    addAP=bucle(alapivots,2)
    addP=bucle(pivots,3)
    for j in addB:
        Jugador.objects.filter(idJugador=j.idJugador).update(usuarios=usuario)
    for j in addE:
        Jugador.objects.filter(idJugador=j.idJugador).update(usuarios=usuario)
    for j in addA:
        Jugador.objects.filter(idJugador=j.idJugador).update(usuarios=usuario)
    for j in addAP:
        Jugador.objects.filter(idJugador=j.idJugador).update(usuarios=usuario)
    for j in addP:
        Jugador.objects.filter(idJugador=j.idJugador).update(usuarios=usuario)      
  
  
def bucle(col,num): 
    res=[]
    while num>0:
        n=randrange(len(col))
        res.append(col[n])
        num=num-1
    return res


def eliminar_usuario(usuario):
    user=User.objects.get(username="Agente libre")
    agente=Usuario.objects.get(user=user)
    jugadores=Jugador.objects.filter(usuarios=usuario)
    for j in jugadores:
        Jugador.objects.filter(idJugador=j.idJugador).update(usuarios=agente)
        
    usuario.delete()
def get_puntuacion(usuario): 
    print("Entro en getPuntuacion")
#     user=User.objects.get(username=nombre)
#     usuario=Usuario.objects.get(user=user)
    alineaciones=Alineacion.objects.filter(usuarios=usuario).exclude(tipoAlineacion='E')
    if not alineaciones:
        return 0
    else:
        res=0
        for a in alineaciones:
            res=res+a.puntuacion
        return res
def nombreValido(nombre):
    return not 'AGENTE' in nombre.upper()
def addUsuario(liga):
    print('Creando agente')
    agentes=User.objects.filter(username__contains='Agente')
    tam=len(agentes)+1
    username='Agente libre '+str(tam)
    user=User.objects.create(first_name="Administrador",last_name="Administrador",username=username,email="administrador@gmail.com",password="administrador")
    user.set_password('administrador')
    user.save()
    u=Usuario.objects.create(user=user,presupuesto=0,liga=liga)
    Alineacion.objects.create(tipoAlineacion='E',usuarios=u)   
    print('Agente creado')
def addJugadores(liga):
    print('Creando jugadores')
    usuario=Usuario.objects.get(user__username__contains='Agente',liga=liga)
    ligas=Liga.objects.all()
    pLiga=ligas[0]
    jugadores= Jugador.objects.filter(liga=pLiga)
    for j in jugadores:
        print(j)
        Jugador.objects.create(nombreJugador=j.nombreJugador,apellidosJugador=j.apellidosJugador,pais=j.pais,equipo=j.equipo,posicion=j.posicion,valor=j.valor,valorMercado=j.valorMercado,puntuacion=j.puntuacion,totalPuntuacion=j.totalPuntuacion,liga=liga,usuarios=usuario)
   