# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from main.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    idLiga = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )  
    
            
    
def crear_tupla(jugadores):
    res=[]
    for j in jugadores:
        tupla=(j.idJugador,j.nombreJugador+" "+j.apellidosJugador)
        res.append(tupla)
    return res


class PujaForm(ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput)
    valorReal= forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = Puja
        fields = ['valor']
        
    def __init__(self, *args, **kwargs):
        super(PujaForm, self).__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance and instance.idPuja:
            self.fields["id"].initial = instance.idPuja
            self.fields["valorReal"].initial= instance.jugadores.valor 
    def clean(self): 
  
        # data from the form is fetched using super function 
        super(PujaForm, self).clean() 
          
        # extract the username and text field from the data 
        idP=self.cleaned_data.get('id')
        print(idP)
        valorPuja = self.cleaned_data.get('valor') 
        print(valorPuja)
        puja=Puja.objects.get(idPuja=idP)
        print(puja)
        valor=puja.jugadores.valor
        print(valor)
  
        # conditions to be met for the username length 
        if valorPuja<valor: 
            self._errors['valor'] = self.error_class([ 
                'No puedes ofrecer menos que su valor']) 
        # return any errors if found 
        return self.cleaned_data   
class LigaForm(ModelForm):
    CHOICES=[('N','Nueva'),
         ('E','Existente')]
    estrategia=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    class Meta:
        model = Liga
        fields = ['tipoLiga']
        widgets = {
        'tipoLiga': forms.RadioSelect
        }
class Liga2Form(ModelForm):

    class Meta:
        model = Liga
        fields = ['nombreLiga','passwordLiga','estrategiaLiga','tipoLiga']
        widgets = {
        'nombreLiga':forms.TextInput(attrs={ 'required': 'true' }),
        'estrategiaLiga': forms.RadioSelect(attrs={ 'required': 'true' }),
        'passwordLiga':forms.PasswordInput(attrs={ 'required': 'true' }),
        'tipoLiga':forms.HiddenInput
        }
    def __init__(self, *args, **kwargs):
        super(Liga2Form, self).__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance:
            self.fields["tipoLiga"].initial = instance
    def is_valid(self):
 
        # run the parent validation first
        valid = super(Liga2Form, self).is_valid()
 
        # we're done now if not valid
        if not valid:
            return valid
 
        # so far so good, get this user based on the username or email
        try:
            liga = Liga.objects.get(nombreLiga=self.cleaned_data['nombreLiga'])
            self._errors['exist'] = 'Liga ya existente'
        # no user with this username or email address
        except Exception:
            
            return True
 
        # verify the passwords match

 
        # all good
        return False
            
class Liga3Form(ModelForm):

    class Meta:
        model = Liga
        fields = ['nombreLiga','estrategiaLiga','tipoLiga']
        widgets = {
        'nombreLiga':forms.TextInput(attrs={ 'required': 'true' }),
        'estrategiaLiga': forms.RadioSelect(attrs={ 'required': 'true' }),
        'tipoLiga':forms.HiddenInput
        }
    def __init__(self, *args, **kwargs):
        super(Liga3Form, self).__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance:
            self.fields["tipoLiga"].initial = instance
    def is_valid(self):
 
        # run the parent validation first
        print('Entro valida Form3')
        valid = super(Liga3Form, self).is_valid()
 
        # we're done now if not valid
        if not valid:
            return valid
 
        # so far so good, get this user based on the username or email
        print('paso el valid del super')
        try:
            print('Buscar si existe la liga')
            liga = Liga.objects.get(nombreLiga=self.cleaned_data['nombreLiga'])
            self._errors['exist'] = 'Liga ya existente'
            
 
        # no user with this username or email address
        except Exception:
            print('Entro en exept')
            return True
 
        # verify the passwords match

 
        # all good
        print('Salio de todo del valid')
        return False
