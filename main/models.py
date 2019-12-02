from django.db import models
from  django.contrib.auth.models  import  User
from django.template.defaultfilters import default


class Liga(models.Model):
    idLiga=models.AutoField(primary_key=True)
    nombreLiga = models.CharField(max_length=30,unique=True)
    passwordLiga = models.CharField(max_length=8,null=True)
    tipoLiga= models.CharField(max_length=2, default='PB',choices=(('PB', 'Publica'),('PR','Privada'),))
    estrategiaLiga= models.CharField(max_length=1,default='2', choices=(('1', 'Millones'),('2','ConEquipo'),))
    def __unicode__(self):
        return unicode(self.nombreLiga)
class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    presupuesto= models.IntegerField(null=True)
    liga= models.ForeignKey(Liga)
    def __unicode__(self):
        return unicode(self.user.username)
    
    
class Jugador(models.Model):
    idJugador =models.AutoField(primary_key=True)
    nombreJugador = models.CharField(max_length=30)
    apellidosJugador = models.CharField(max_length=8)
    pais = models.CharField(max_length=20)
    equipo = models.CharField(max_length=20)
    posicion = models.CharField(max_length= 20)
    valor = models.PositiveIntegerField()
    valorMercado = models.PositiveIntegerField()
    puntuacion= models.IntegerField()
    mercado=models.BooleanField(default=False)
    totalPuntuacion= models.IntegerField()
    liga= models.ForeignKey(Liga)
    usuarios= models.ForeignKey(Usuario)
    alineaciones=models.ManyToManyField('Alineacion',null=True)
    def __unicode__(self):
        return unicode(self.nombreJugador)

class Puja(models.Model):
    idPuja=models.AutoField(primary_key=True)
    estadoPuja= models.CharField(max_length=2, choices=(('A', 'Aceptada'),('P', 'Pendiente'),('R','Rechazada'),))
    fechaPuja= models.DateTimeField(auto_now= True)
    valor= models.PositiveIntegerField(default=0)
    pujador= models.ForeignKey(Usuario,related_name="pujador_puja")
    ofertante= models.ForeignKey(Usuario,related_name="ofertante_puja")
    jugadores= models.ForeignKey(Jugador)
    def __unicode__(self):
        return unicode(self.idPuja)     
    
class Alineacion(models.Model):
    idAlinecion=models.AutoField(primary_key=True)
    fechaAlineacion= models.DateTimeField(auto_now= True)
    puntuacion = models.FloatField(default=0)
    orden = models.TextField(blank=True,null=True)
    tipoAlineacion= models.CharField(max_length=1, choices=(('E', 'Editable'),('D','No editable'),))
    jugadores=models.ManyToManyField(Jugador,null=True,blank=True)
    usuarios= models.ForeignKey(Usuario)
    def __unicode__(self):
        return unicode(self.idAlinecion)
    
class Mensaje(models.Model):
    idMensaje=models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=30)
    contenido = models.TextField(max_length=200)
    autor= models.CharField(max_length= 20)
    liga= models.ForeignKey(Liga)
    def __unicode__(self):
        return unicode(self.asunto) 