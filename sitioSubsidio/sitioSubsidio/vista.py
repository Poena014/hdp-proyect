from django.http import  HttpResponse, HttpRequest, QueryDict
from django.template import Template,Context
from  django.shortcuts import  render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from cuestionarios.models import  cuestionario, pregunta, item_pregunta, registro, registrado
from consultasubsidio.models import  documento, departamento, municipio, subsidios, aplica
from datetime import datetime

fechaget=datetime.now().date()



#import os
#script_dir = os.path.dirname(__file__)
#rel_path = "templates/index.html"
#abs_file_path = os.path.join(script_dir, rel_path)


def inicio(request):
    
    return render(request, "index.html")

def encuestas(request):
    cuestio1= cuestionario.objects.all()
    contexto= {'datos_cuestionarios': cuestio1}
    return render(request, "encuestas.html",contexto)

def encuestasr(request, id):
    cuestio1= cuestionario.objects.get(id=id)
    preguns= pregunta.objects.filter(cuestionario_id=id)
    items=[]
    for i in preguns:
        items.append (item_pregunta.objects.filter(preguntas_id=i))
    contexto= {'cuestionario': cuestio1, 'preguntas': preguns, 'items': items}
    return render(request, "encuestar.html",contexto)


def registro_encuesta(request):
    if request.method == "POST":
        valores= request.POST.items()
        regis= registro(fecha=fechaget)
        regis.save()
        for valor in valores:
            idget, dato=valor
            if idget.isdigit():
                item=item_pregunta.objects.get(id=idget)

                preg=pregunta.objects.get(id= item.preguntas.id )

                cues=cuestionario.objects.get( id=preg.cuestionario.id)
                final=registrado(registros=regis, cuestionarios=cues, preguntas=preg, item_preguntas= item, guardado=dato )
                final.save()

    return render(request, "index.html" )

def consultas(request):

    subs=subsidios.objects.all()



    contexto={ 'subsidios':subs}
    return render(request, "consultas.html", contexto)

def infoconsulta(request, id):

    subs=subsidios.objects.get(id=id)
    datos=[]
    nombres=[]
    for m in range(1, 15):
        valor=aplica.objects.filter(persona__depar__id=m, subsidio_id=id).count()
        valor2=departamento.objects.get(id=m)
        datos.append(valor)
        nombres.append(valor2.nombre)

    contexto={ 'sub':subs  , 'datos':datos, 'depars':nombres}
    return render(request, "consultasr.html", contexto)

def acerca(request):
    
    return render(request, "contactanos.html")

@login_required(login_url="/login/")
def lossubsidios(request):

    usuario=request.user
    doc=documento.objects.filter(usuario_id=usuario.id).first()
    aplico=aplica.objects.filter(persona__dui=doc.dui)


    contexto= {'datos': doc, 'subsidios': aplico}
    return render(request, "subsidios.html", contexto)


def logins(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, "login.html")


def salir(request):
    logout(request)
    return redirect('/')



def configuracion(request):

    usuario=request.user
    grupo=str(usuario.groups.get())

    contexto={}
    valor=False
    print(grupo)
    if grupo == "Administrador":
        subs=documento.objects.all().order_by('dui')
        valor=True
        contexto={ 'usuarios': subs, 'tipo': valor }
    else:
        valor=False
        contexto={ 'tipo': valor }

    if request.method == 'POST':
        valores= request.POST.items()
        for valor in valores:
            idget, dato=valor
            idget=str(idget)
            if idget=="id":
                User.objects.filter(id=dato).delete()

    return render(request, "configuracion.html", contexto)
            
def configuracionsub(request):

    usuario=request.user
    grupo=str(usuario.groups.get())

    contexto={}
    valor=False
    print(grupo)
    if grupo == "Administrador":
        subs=subsidios.objects.all().order_by('nombre')
        valor=True
        contexto={ 'subsidios': subs, 'tipo': valor }
    else:
        valor=False
        contexto={ 'tipo': valor }

    if request.method == 'POST':
        valores= request.POST.items()
        for valor in valores:
            idget, dato=valor
            idget=str(idget)
            if idget=="id":
                subsidios.objects.filter(id=dato).delete()

    return render(request, "configsubsidio.html", contexto)

def configuracionenc(request):

    usuario=request.user
    grupo=str(usuario.groups.get())

    contexto={}
    valor=False
    print(grupo)
    if grupo == "Administrador":
        subs=cuestionario.objects.all().order_by('nombre')
        valor=True
        contexto={ 'cuestionarios': subs, 'tipo': valor }
    else:
        valor=False
        contexto={ 'tipo': valor }

    if request.method == 'POST':
        valores= request.POST.items()
        for valor in valores:
            idget, dato=valor
            idget=str(idget)
            if idget=="id":
                cuestionario.objects.filter(id=dato).delete()

    return render(request, "configencuestas.html", contexto)

def configuracionaplica(request):

    usuario=request.user
    grupo=str(usuario.groups.get())

    contexto={}
    valor=False
    print(grupo)
    if grupo == "Administrador":
        valores=aplica.objects.all()
        valor=True
        contexto={ 'aplicas': valores, 'tipo': valor }
    else:
        valor=False
        contexto={ 'tipo': valor }


    if request.method == 'POST':
        valores= request.POST.items()
        for valor in valores:
            idget, dato=valor
            idget=str(idget)
            if idget=="id":
                aplica.objects.filter(id=dato).delete()

    return render(request, "configaplica.html", contexto)    


    
def addencuesta(request):
    if request.method == 'POST':
        nom = request.POST['nombre']
        fec=request.POST['fecha']
        des=request.POST['descripcion']

        #bolean
        estado = request.POST['estado']
        alc = request.POST['alcance']

        enc=cuestionario(nombre=nom, estado=estado, fecha=fec, descripcion=des, alcance=alc)
        enc.save()
        return redirect("/configuraciones/encuesta")
    else:
        return render(request, "encuestaadd.html")

def addsubsidio(request):
    if request.method == 'POST':
        nom = request.POST['nombre']
        fec=request.POST['fecha']
        des=request.POST['descripcion']

        #bolean
        estado = request.POST['estado']
        alc = request.POST['alcance']

        enc=cuestionario(nombre=nom, estado=estado, fecha=fec, descripcion=des, alcance=alc)
        enc.save()
        return redirect("/configuraciones/encuesta")
    else:
        return render(request, "subsidioadd.html")
    
    return render(request, "contactanos.html")

def addaplica(request):
    
    return render(request, "contactanos.html")

def addusuario(request):
    
    return render(request, "contactanos.html")

