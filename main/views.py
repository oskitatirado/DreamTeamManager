
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
import csv
import pandas as pd
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404,HttpResponse
from django.template import RequestContext
from django_pandas.io import read_frame
from main.forms import PujaForm,SignUpForm,LigaForm,Liga2Form,Liga3Form
from main.models import *
from main.populate import populateDatabase
from random import shuffle
from main.utils import *
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.tasks import *



    
#  CONJUNTO DE VISTAS

def index(request): 
    
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    return render_to_response('index.html')

def add(request): 
    liga=Liga.objects.get(nombreLiga="Liga de Prueba")
    userr=User.objects.create(first_name="Antonio",last_name="Chaps",username="antonio",email="antonio@gmail.com",password="100119996")
    userr.set_password('10011996')
    userr.save()
    user=Usuario.objects.create(user=userr,presupuesto=0,liga=liga)
    Alineacion.objects.create(tipoAlineacion='E',usuarios=user)
    add_jugadores(user,liga)
    return render_to_response('index.html')

def rem(request): 
    user=User.objects.get(username="paquito")
    usuario=Usuario.objects.get(user=user)
    eliminar_usuario(usuario)
    return render_to_response('index.html')

def populateDB(request):
    populateDatabase() 
    return render_to_response('populate.html')

@login_required
def agentesLibres(request):
    user=request.user
    usuario=Usuario.objects.get(user=user)
    return render_to_response('listaJugadores.html',{'usuario':usuario})

@login_required
def form_alin(request):
    user=request.user
    usuario=Usuario.objects.get(user=user)
    alineacion=Alineacion.objects.get(usuarios=usuario,tipoAlineacion='E')
    orden=alineacion.orden
    if orden != None:
        posicion=orden.split('#')
    else:
        posicion=[]
    
    
    jugadores=Jugador.objects.filter(usuarios=usuario)
    bases=jugadores.filter(posicion='B')
    if posicion:
        idBase=posicion[0]
    else:
        idBase='NULL'    
    if idBase== 'NULL':
        idBase=-1
    escoltas=jugadores.filter(posicion__contains="E")
    if posicion:
        idEscolta=posicion[1]
    else:
        idEscolta='NULL'
    if idEscolta== 'NULL':
        idEscolta=-1
    aler=jugadores.filter(posicion__contains="A")
    aleros=aler.exclude(posicion="AP")
    if posicion:
        idAlero=posicion[2]
    else:
        idAlero='NULL'
    if idAlero== 'NULL':
        idAlero=-1
    alapivots=jugadores.filter(posicion="AP")
    if posicion:
        idAP=posicion[3]
    else:
        idAP='NULL'
    if idAP== 'NULL':
        idAP=-1
    pivots=jugadores.filter(posicion="P")
    if posicion:
        idPivot=posicion[4]
    else:
        idPivot='NULL'
    if idPivot== 'NULL':
        idPivot=-1
    suplente1=bases.exclude(idJugador=idBase)
    if posicion:
        idS1=posicion[5]
    else:
        idS1='NULL'
    if idS1== 'NULL':
        idS1=-1
    suplente2=escoltas.exclude(idJugador=idEscolta)
    if posicion:
        idS2=posicion[6]
    else:
        idS2='NULL'
    if idS2== 'NULL':
        idS2=-1
    suplente3=aleros.exclude(idJugador=idAlero)
    if posicion:
        idS3=posicion[7]
    else:
        idS3='NULL'
    if idS3== 'NULL':
        idS3=-1
    suplente4=alapivots.exclude(idJugador=idAP)
    if posicion:
        idS4=posicion[8]
    else:
        idS4='NULL'
    if idS4== 'NULL':
        idS4=-1
    suplente5=pivots.exclude(idJugador=idPivot)
    if posicion:
        idS5=posicion[9]
    else:
        idS5='NULL'
    if idS5== 'NULL':
        idS5=-1
    escoltas=escoltas.exclude(idJugador=idAlero)
    aleros=aleros.exclude(idJugador=idEscolta)
    suplente2=suplente2.exclude(idJugador=idAlero).exclude(idJugador=idS3)
    suplente3=suplente3.exclude(idJugador=idEscolta).exclude(idJugador=idS2)
    jugadores=jugadores.order_by('posicion')
    print(idBase,idEscolta,idAlero,idAP,idPivot,idS1,idS2,idS3,idS4,idS5)    
    return render_to_response('search_user2.html', {'jugadores':jugadores,'bases':bases , 'escoltas':escoltas ,'aleros':aleros,'alapivots':alapivots,'pivots':pivots,'suplentes1':suplente1,'suplentes2':suplente2,'suplentes3':suplente3,'suplentes4':suplente4,'suplentes5':suplente5,'b':int(idBase),'e':int(idEscolta),'a':int(idAlero),'ap':int(idAP),'p':int(idPivot),'bs':int(idS1),'es':int(idS2),'as':int(idS3),'aps':int(idS4),'ps':int(idS5)}, context_instance=RequestContext(request))



@login_required
def suplente(request):
    print("entro en el ajax")
    base=request.POST['base']
    escolta=request.POST['escolta']
    alero=request.POST['alero']
    ap=request.POST['ap']
    pivot=request.POST['pivot']
    bs=request.POST['s1']
    es=request.POST['s2']
    alers=request.POST['s3']
    aps=request.POST['s4']
    ps=request.POST['s5']
    user=request.user
    usuario=Usuario.objects.get(user=user)
    jugadores=Jugador.objects.filter(usuarios=usuario)
    bases=jugadores.filter(posicion='B')
    escoltas=jugadores.filter(posicion__contains="E")
    aler=jugadores.filter(posicion__contains="A")
    aleros=aler.exclude(posicion="AP")
    alapivots=jugadores.filter(posicion="AP")
    pivots=jugadores.filter(posicion="P")
    print(base,escolta,alero,ap,pivot,bs,es,alers,aps,ps)
    if base!= '-1':
        suplente1=bases.exclude(idJugador=base)
    else:
        suplente1=bases
    if escolta!='-1':
        suplente2=escoltas.exclude(idJugador=escolta)
    else:
        suplente2=escoltas
    if alero != '-1':
        suplente3=aleros.exclude(idJugador=alero)
    else:
        suplente3=aleros
    if ap != '-1':
        suplente4=alapivots.exclude(idJugador=ap)
    else:
        suplente4= alapivots
    if pivot != '-1':
        suplente5=pivots.exclude(idJugador=pivot)
    else:
        suplente5=pivots
    escoltas=escoltas.exclude(idJugador=alero)
    aleros=aleros.exclude(idJugador=escolta)
    suplente2=suplente2.exclude(idJugador=alero).exclude(idJugador=alers)
    suplente3=suplente3.exclude(idJugador=escolta).exclude(idJugador=es)
    jugadores=jugadores.order_by('posicion')
    return render_to_response('search_user2.html', {'jugadores':jugadores,'bases':bases , 'escoltas':escoltas ,'aleros':aleros,'alapivots':alapivots,'pivots':pivots,'suplentes1':suplente1,'suplentes2':suplente2,'suplentes3':suplente3,'suplentes4':suplente4,'suplentes5':suplente5,'b':int(base),'e':int(escolta),'a':int(alero),'ap':int(ap),'p':int(pivot),'bs':int(bs),'es':int(es),'as':int(alers),'aps':int(aps),'ps':int(ps)}, context_instance=RequestContext(request))
@login_required
def guardarAlineacion(request):
    print("Entro en gardaralineacion")
    if not '_vender' in request.POST:
        user=request.user
        usuario=Usuario.objects.get(user=user)
        base=request.POST.get('base','')
        escolta=request.POST.get('escolta','')
        alero=request.POST.get('alero','')
        ap=request.POST.get('ap','')
        pivot=request.POST.get('pivot','')
        baseS=request.POST.get('baseS','')
        escoltaS=request.POST.get('escoltaS','')
        aleroS=request.POST.get('aleroS','')
        apS=request.POST.get('apS','')
        pivotS=request.POST.get('pivotS','')
        print('BaseS:',baseS)
        alineacion=Alineacion.objects.get(usuarios=usuario,tipoAlineacion='E')
        alineacion.jugadores.clear()
        orden=""
        if base != '-1'and base != '':
            baseSaved=Jugador.objects.get(idJugador=base)
            alineacion.jugadores.add(baseSaved)
            orden+= base+"#"
        else:
            orden+="NULL#"
        if escolta != '-1' and escolta != '':
            escoltaSaved=Jugador.objects.get(idJugador=escolta)
            alineacion.jugadores.add(escoltaSaved)
            orden+= escolta+"#"
        else:
            orden+="NULL#"
        if alero != '-1'and alero != '':
            aleroSaved=Jugador.objects.get(idJugador=alero)
            alineacion.jugadores.add(aleroSaved)
            orden+= alero+"#"
        else:
            orden+="NULL#"
        if ap != '-1' and ap != '':
            apSaved=Jugador.objects.get(idJugador=ap)
            alineacion.jugadores.add(apSaved)
            orden+= ap+"#"
        else:
            orden+="NULL#"
        if pivot != '-1' and pivot != '':
            pivotSaved=Jugador.objects.get(idJugador=pivot)
            alineacion.jugadores.add(pivotSaved)
            orden+= pivot+"#"
        else:
            orden+="NULL#"
       
        if baseS != '-1'  and baseS != '':
            baseSSaved=Jugador.objects.get(idJugador=baseS)
            alineacion.jugadores.add(baseSSaved)
            orden+= baseS+"#"
        else:
            orden+="NULL#"
        if escoltaS != '-1'  and escoltaS != '':
            escoltaSSaved=Jugador.objects.get(idJugador=escoltaS)
            alineacion.jugadores.add(escoltaSSaved)
            orden+= escoltaS+"#"
        else:
            orden+="NULL#"
        if aleroS != '-1'  and aleroS != '':
            aleroSSaved=Jugador.objects.get(idJugador=aleroS)
            alineacion.jugadores.add(aleroSSaved)
            orden+= aleroS+"#"
        else:
            orden+="NULL#"
        if apS != '-1'  and apS != '':
            apSSaved=Jugador.objects.get(idJugador=apS)
            alineacion.jugadores.add(apSSaved)
            orden+= apS+"#"
        else:
            orden+="NULL#"
        if pivotS != '-1'  and pivotS != '':
            pivotSSaved=Jugador.objects.get(idJugador=pivotS)
            alineacion.jugadores.add(pivotSSaved)
            orden+= pivotS
        else:
            orden+="NULL"
        alineacion.orden=orden
        alineacion.save()
       
        return HttpResponseRedirect('/create/alineacion')
    else:
        return addMercado(request)
@login_required 
def crear_mercado(request):
    print("Creacion mercado")
    usuario=Usuario.objects.get(user=request.user)
    crearMercado(usuario.liga)
    print("mercado creado")
    return render_to_response('index.html', context_instance=RequestContext(request))

@login_required
def mercado(request):
    print("lista mercado")
    usuario=Usuario.objects.get(user=request.user)
    jugadores=Jugador.objects.filter(mercado=True,liga=usuario.liga)
    print("salida lista mercado")
    return render_to_response('mercado.html', {'jugadores':jugadores}, context_instance=RequestContext(request))
@login_required
def crearPuja(request,jugadorId):
    print("Entro crear puja")
    jugador=Jugador.objects.get(idJugador=jugadorId)
    user=request.user
    usuario=Usuario.objects.get(user=user)
    try:
        
        puja=Puja.objects.get(estadoPuja='P',pujador=usuario,jugadores=jugador,ofertante=jugador.usuarios)
    except:
        puja=Puja.objects.create(estadoPuja='P',pujador=usuario,ofertante=jugador.usuarios,jugadores=jugador,valor=jugador.valorMercado)
    print(puja.idPuja)
    form = PujaForm(instance=puja)
    print(form)

    
    print(jugador)
    return render_to_response('puja.html', {'form': form}, context_instance=RequestContext(request))
@login_required
def puja(request):
    if request.method=='POST':
        form = PujaForm(request.POST, request.FILES)
        if form.is_valid():
            if '_guardar' in request.POST:
                print("Entro en crear/editar")
                idP = form.cleaned_data['id']
                valor = form.cleaned_data['valor']
                puja = get_object_or_404(Puja, idPuja=idP)
                puja.valor=valor
                puja.save()
                print(puja)
                l=reverse('mercadoDeJugadores')
                print(l)
                return HttpResponseRedirect(l)
            elif '_cancelar' in request.POST:
                print("Entro en cancelar")
                idP = form.cleaned_data['id']
                puja = get_object_or_404(Puja, idPuja=idP)
                puja.delete()
                l=reverse('mercadoDeJugadores')
                print(l)
                return HttpResponseRedirect(l)
        else:
            return render_to_response('puja.html', {'form': form}, context_instance=RequestContext(request))        
    else:
        form=PujaForm(instance=puja)
        return render_to_response('puja.html', {'form': form}, context_instance=RequestContext(request))
def darValor(request):
    mercado=Jugador.objects.filter(mercado=True)
    for j in mercado:
        j.valor=3000000
        j.valorMercado=5000000
        j.save()
    l=reverse('mercadoDeJugadores')
    print(l)
    return HttpResponseRedirect(l)
@login_required
def aceptarPuja(request,pujaId):
    puja=Puja.objects.get(idPuja=pujaId)
    jugador=puja.jugadores
    restos=Puja.objects.filter(jugadores=jugador).exclude(idPuja=puja.idPuja)
    if restos:
        for p in restos:
            p.estadoPuja='R'
            p.save()
    puja.estadoPuja='A'
    jugador.usuarios=puja.pujador
    jugador.mercado=False
    puja.save()
    jugador.save()
    l=reverse('misPujas')
    print(l)
    return HttpResponseRedirect(l)
@login_required
def rechazarPuja(request,pujaId):
    puja=Puja.objects.get(idPuja=pujaId)
    puja.estadoPuja='R'
    puja.save()
    l=reverse('misPujas')
    print(l)
    return HttpResponseRedirect(l)
@login_required
def misPujas(request):
    user=request.user
    agente=Usuario.objects.get(user=user)
    ofertas=Puja.objects.filter(ofertante=agente)
    solicitudes=Puja.objects.filter(pujador=agente)
    return render_to_response('Mispuja.html', {'ofertas': ofertas,'solicitudes':solicitudes}, context_instance=RequestContext(request))
@login_required
def addMercado(request):
    print("Entro en addMercado")
    idJ=request.POST.get('id_jugador','')
    print(idJ)
    valor=request.POST.get('valor','')
    print(valor)
    jugador=Jugador.objects.get(idJugador=int(idJ))
    jugador.valorMercado=valor
    jugador.mercado=True
    jugador.save()
    l=reverse('alineacionList')
    print(l)
    return HttpResponseRedirect(l)
@login_required   
def vender(request,jugadorId):
    j=Jugador.objects.get(idJugador=jugadorId)
    return render_to_response('vender.html', {'id': jugadorId,'precio':j.valor}, context_instance=RequestContext(request))

@login_required   
def quitarMercado(request,jugadorId):
    j=Jugador.objects.get(idJugador=jugadorId)
    j.valorMercado=j.valor
    j.mercado=False
    j.save()
    l=reverse('alineacionList')
    print(l)
    return HttpResponseRedirect(l) 
@login_required
def ofrecer(request):
    user=User.objects.get(username="Agente libre")
    agente=Usuario.objects.get(user=user)
    enVenta=Jugador.objects.filter(mercado=True).exclude(usuarios=agente)
    if enVenta:
        for j in enVenta:
            Puja.objects.create(estadoPuja='P',pujador=agente,ofertante=j.usuarios,jugadores=j,valor=j.valor)
    l=reverse('misPujas')
    print(l)
    return HttpResponseRedirect(l)
@login_required   
def clasificacion(request):
    user=request.user
    usuario=Usuario.objects.get(user=user)
    liga=Liga.objects.get(idLiga=usuario.liga.idLiga)
   # nop=User.objects.get(username="Agente libre")
    #agente=Usuario.objects.get(user=nop)
    usuarios2=Usuario.objects.filter(liga=liga).exclude(user__username__contains='Agente')
    usuarios=list(usuarios2)
    #usuarios.remove(agente)
    dicc={}
    for u in usuarios:
        dicc[u]=get_puntuacion(u)
    sorted_d = sorted(dicc.items(), key=lambda x: x[1],reverse=True)
    
    return render_to_response('clasificacion.html',{'usuarios': sorted_d},context_instance=RequestContext(request))
@login_required   
def clasificacionSemanal(request):
    print('Entro en clasificacion Semanal')
    user=request.user
    usuario=Usuario.objects.get(user=user)
    alineaciones=Alineacion.objects.filter(usuarios=usuario,tipoAlineacion='D').order_by('-fechaAlineacion')
    if alineaciones:
        alineacion=alineaciones[0]
        trozos2=alineacion.orden.split('#')
        trozos=[]
        for t in trozos2:
            if not t =='NULL':
                trozos.append(int(t))
            else:
                trozos.append(int(-1))
        titulares=trozos[:5]
        suplentes=trozos[5:]
        jugadores=alineacion.jugadores.all()
        print(titulares)
        
        return render_to_response('clasificacionSemanal.html',{'jugadores':jugadores,'puntuacion':alineacion.puntuacion,'titulares':titulares,'suplentes':suplentes},context_instance=RequestContext(request))
    else:
        return render_to_response('clasificacionSemanal.html',{'error':'No tienes guardada aun ninguna alineacion'},context_instance=RequestContext(request))
    
def guardar_alin_semanal(request):
    ligas= Liga.objects.all()
    for liga in ligas:
        jugadores=Usuario.objects.filter(liga=liga).exclude(user__username__contains='Agente')
        print(jugadores)
        for usuario in jugadores:
            alineacion=Alineacion.objects.get(usuarios=usuario,tipoAlineacion='E')
            alineacionSaved=Alineacion.objects.create(tipoAlineacion='D',usuarios=usuario,orden=alineacion.orden)
            alineacionSaved.jugadores.add(*alineacion.jugadores.all())
            alineacionSaved.save()
            
    l=reverse('index')
    print(l)
    return HttpResponseRedirect(l)
def listing(request):
    liga=Liga.objects.all()
    jugadores = Jugador.objects.filter(liga=liga[0]).order_by('equipo')
    paginator = Paginator(jugadores, 20) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('puntuacion.html', {"contacts": contacts},context_instance=RequestContext(request))

def cargarPuntuacion(request):
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            print("No es csv file")
#             messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("listinga"))
        #if file is too large, return
        if csv_file.multiple_chunks():
            print("csv demasiado grande")
#             messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("listinga"))

        file_data = csv_file.read().decode("utf-8")        

        lines = file_data.split("\n")
        dele=lines[0]
        lines.remove(dele)
        #loop over the lines and save them in db. If error , store as string and then display
        for line in lines:                        
            fields = line.split(";")
           
            nombre=fields[0]
            apellido=fields[1]
            puntuacion=int(fields[3])
            
            try:
                jugadores=Jugador.objects.filter(nombreJugador=nombre,apellidosJugador=apellido)
                print(jugadores)
                print(puntuacion)
                if jugadores:
                    for j in jugadores:
                        oldP=j.totalPuntuacion
                        j.puntuacion=puntuacion
                        j.totalPuntuacion=oldP+puntuacion
                        j.save()
                                                          
            except Exception as e:    
                print(e)             
                pass
        

    except Exception as e:
        print('A ocurrido un error')
        print(e)
#         logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
#         messages.error(request,"Unable to upload file. "+repr(e))
    actualizar_puntuacion()
    print("Salio bien")
    return HttpResponseRedirect(reverse("listinga"))

def dowmload_csv(request):
    liga=Liga.objects.all()
    jugadores=Jugador.objects.filter(liga=liga[0]).order_by('equipo')   
    df = read_frame(jugadores, fieldnames=['nombreJugador', 'apellidosJugador', 'equipo','puntuacion'])
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="puntuacion.csv"'
    df.to_csv(path_or_buf=response,sep=';',float_format='%.2f',index=False,decimal=",")
    
    return response

def signup(request,ligaId):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if nombreValido(form.cleaned_data.get('username')):
                form.save()
                username = form.cleaned_data.get('username')
                userr=User.objects.get(username=username)
                liga=Liga.objects.get(idLiga=form.cleaned_data.get('idLiga'))
                if liga.estrategiaLiga=='1':
                    pres=40000000
                else:
                    pres=20000000
                user=Usuario.objects.create(user=userr,presupuesto=pres,liga=liga)
                Alineacion.objects.create(tipoAlineacion='E',usuarios=user)
                if liga.estrategiaLiga=='2':
                    add_jugadores(user,liga)
                
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                
                #Falta crear usuario con ese user pero depende del tipo de liga
                l=reverse('alineacionList')
                print(l)
                return HttpResponseRedirect(l)
    else:
        form = SignUpForm({'idLiga':ligaId})
    return render_to_response('signup.html', {'form': form},context_instance=RequestContext(request))
def registroLiga(request):
    print(request.path)
    form = LigaForm({'estrategia':'N','tipoLiga':'PB'})
    return render_to_response('tipoLiga.html', {'form': form},context_instance=RequestContext(request))

def privada(request):
    if request.method == 'POST':
        nombreLiga=request.POST.get('nombreLiga','')
        passwordLiga=request.POST.get('passwordLiga','')
        try:
            liga=Liga.objects.get(tipoLiga='PR',nombreLiga=nombreLiga,passwordLiga=passwordLiga)
        except Exception as e:
            return render_to_response('ligaPrivada.html',{'error':'No existe la liga'},context_instance=RequestContext(request))
        l=reverse('signup', kwargs={'ligaId': liga.idLiga})
        print(l)
        return HttpResponseRedirect(l)
    else:
        return render_to_response('ligaPrivada.html',context_instance=RequestContext(request))
def tipoLiga(request):

    if request.method=='POST':
        form = LigaForm(request.POST, request.FILES)
        if form.is_valid():
            tipo = form.cleaned_data['tipoLiga']
            estrategia = form.cleaned_data['estrategia']
            if tipo=='PB' and estrategia=='N':
                #Creacion liga
                form=Liga3Form({'tipoLiga':tipo})
                return render_to_response('liga.html', {'form': form},context_instance=RequestContext(request))
            
            
            if tipo=='PB' and estrategia=='E':
                #ligas=Liga.objects.filter(tipoLiga='PB')
                ligas=Liga.objects.all()
                shuffle(ligas)
                liga=ligas[0]
                l=reverse('signup', kwargs={'ligaId': liga.idLiga})
                print(l)
                return HttpResponseRedirect(l)
                
            
            if tipo=='PR' and estrategia=='N':
                #creacion liga
                form=Liga2Form({'tipoLiga':tipo})
                return render_to_response('liga.html', {'form': form},context_instance=RequestContext(request))
                
            if tipo=='PR' and estrategia=='E':
                #usuario y contrasena   
                l=reverse('privada')
                print(l)
                return HttpResponseRedirect(l)
def liga(request):
    if request.method == 'POST':
        try:
            tipo=request.POST.get('tipoLiga','')
            if tipo =='PB':
                privada=False
            else:
                privada=True
        except Exception as e:
            print(e)
            privada=False
        if privada:
            print('Entro en privada')
            form = Liga2Form(request.POST)
            if form.is_valid():
                print('Valida')
                liga=Liga.objects.create(nombreLiga=form.cleaned_data['nombreLiga'],tipoLiga='PR',estrategiaLiga=form.cleaned_data['estrategiaLiga'],passwordLiga=form.cleaned_data['passwordLiga'])
                addUsuario(liga)
                addJugadores(liga)
                crearMercado(liga)
                l=reverse('signup', kwargs={'ligaId': liga.idLiga})
                print(l)
                return HttpResponseRedirect(l)
        else:
            print('Entro en publica')        
            form = Liga3Form(request.POST)
            print(form)
            if form.is_valid():
                print('Valida')
                liga=Liga.objects.create(nombreLiga=form.cleaned_data['nombreLiga'],tipoLiga='PB',estrategiaLiga=form.cleaned_data['estrategiaLiga'])
                addUsuario(liga)
                addJugadores(liga)
                crearMercado(liga)
                l=reverse('signup', kwargs={'ligaId': liga.idLiga})
                print(l)
                return HttpResponseRedirect(l)
    print('Salio de todo')
    
    return render_to_response('liga.html', {'form': form},context_instance=RequestContext(request))
        