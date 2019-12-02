from main.models import Liga,Usuario,Jugador, Alineacion

from django.db.transaction import commit_on_success
import os
from  django.contrib.auth.models  import  User
path = "EquiposNBA"


@commit_on_success
def populateLiga():
    print("Cargando liga...")
    Liga.objects.all().delete()
    Liga.objects.create(nombreLiga="Liga de Prueba",tipoLiga='PB',estrategiaLiga='1')
        
    print("Ligas insertadas: " + str(Liga.objects.count()))
    print("---------------------------------------------------------")
    
     
@commit_on_success   
def listar_archivos():
    print("Cargando jugadores...")
    Jugador.objects.all().delete()
    nombres=os.listdir(path)
    for n in nombres:
        populateJugadores(path+"/"+n)
  
@commit_on_success
def populateJugadores(ruta):
    
    fileobj=open(ruta,"r")
    line=fileobj.readline()
    while line:
        partes=line.split("#")
        nombre=partes[0].strip().decode('utf-8', 'replace')
        apellido=partes[1].strip().decode('utf-8', 'replace')
        pais=partes[2].strip().decode('utf-8', 'replace')
        posicion=partes[3].strip().decode('utf-8', 'replace')
        equipo=partes[4].strip().decode('utf-8', 'replace')
        liga=Liga.objects.get(nombreLiga="Liga de Prueba")
        user=User.objects.get(username="Agente libre")
        usuario=Usuario.objects.get(user=user)
        Jugador.objects.create(nombreJugador=nombre,apellidosJugador=apellido,pais=pais,equipo=equipo,posicion=posicion,valor=0,valorMercado=0,puntuacion=0,totalPuntuacion=0,liga=liga,usuarios=usuario)
        line=fileobj.readline()
    fileobj.close()
    print("jugadores insertados: " + str(Jugador.objects.count()))
    print("---------------------------------------------------------")
@commit_on_success
def populateUsuarios():
    print("Cargando usuarios...")
    Usuario.objects.all().delete()
    user=User.objects.create(first_name="Administrador",last_name="Administrador",username="Agente libre",email="administrador@gmail.com",password="administrador")
    liga=Liga.objects.get(nombreLiga="Liga de Prueba")
    user.set_password('administrador')
    user.save()
    u=Usuario.objects.create(user=user,presupuesto=0,liga=liga)
    Alineacion.objects.create(tipoAlineacion='E',usuarios=u)   
    print("usuarios insertadas: " + str(Usuario.objects.count()))
    print("---------------------------------------------------------") 

    
     
def populateDatabase():
    populateLiga()
    populateUsuarios()
    listar_archivos()
    print("Finished database population")
    
if __name__ == '__main__':
    populateDatabase()