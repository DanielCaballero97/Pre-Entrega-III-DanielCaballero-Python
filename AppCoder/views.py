from django.shortcuts import render
from AppCoder.models import Curso , Profesor , Estudiante , Entregable
from AppCoder.forms import Buscar
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse


def profesores(request):
    

     if request.method == 'POST':
      
            Profe =  Profesor(nombre=request.POST['nombre'],
                            email=request.POST['email'],
                            apellido=request.POST['apellido'])
 
            Profe.save()
 
            return render(request, "AppCoder/profesores.html")
 
     return render(request, "AppCoder/profesores.html")



def estudiantes(request):

    if request.method == "POST":
         
         estu = Estudiante(nombre=request.POST['nombre'],
                            email=request.POST['email'],
                            apellido=request.POST['apellido'])
         estu.save()
         return render(request, "AppCoder/estudiantes.html")

    return render(request, "AppCoder/estudiantes.html")



def entregables(request):
    
    if request.method == "POST":
         try:
                check= request.POST["entregado"]
         except MultiValueDictKeyError:
                check= False
         else:
                check=True 
         entre = Entregable(
              nombre=request.POST["nombre"],
              fecha_de_entrega=request.POST["fecha_de_entrega"],
              entregado= check
              )
         entre.save()
         return render(request, "AppCoder/entregables.html")

    return render(request, "AppCoder/entregables.html")



def cursos(request):

    if request.method == 'POST':
      
            curso =  Curso(nombre=request.POST['curso'],
                           camada=request.POST['camada'])
 
            curso.save()
 
            return render(request, "AppCoder/cursos.html")
 
    return render(request,"AppCoder/cursos.html")

def indexResultado(request):
     
     return render (request, "AppCoder/indexResultado.html")


def buscar(request):
    if request.method == "POST":
        miFormulario = Buscar(request.POST)
        if miFormulario.is_valid():
             info = miFormulario.cleaned_data
             curso = Curso.objects.filter(nombre__icontains=info["nombre"])
             return render(request, "AppCoder/index.html" , { 
                  "formulario": miFormulario,
                  "cursos": curso})
             
    else:
        miFormulario = Buscar()

    return render(request, "AppCoder/index.html", {"formulario": miFormulario} )

