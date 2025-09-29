from django.shortcuts import render,redirect
from django.contrib import auth
from sitoWeb.func import main

def Pagina_generale(request):
    return render(request,'main/main.html')

def Pagina_registrazione(request):
    if request.method == "GET":
        return render(request,'registrazione/registrazione.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        risultato_date =main.verifica_date(name=name,password=password)
        if risultato_date == 'La password e Adatta':
            risultato_Unicita = main.verifica_Unicità(name=name,password=password)
            context = { 'risultato_registrazione' : risultato_date, 'risultato_Unicita' : risultato_Unicita}
        else: 
            context = {'risultato_registrazionee' : risultato_date}
        return render(request,'registrazione/registrazione.html',context=context)
    
def Acceso_account(request):
    if request.method == "GET":
        return render(request,'Accesso/Accesso.html')
    elif request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        User = auth.authenticate(username=name,password=password)
        if User is not None:
            auth.login(request,user=User)
            return redirect('Pagina_generale')
        else:
            return render(request,'Accesso/Accesso.html',context={'text':'Non siete entrati nell Account il nome o la password e sbagliata'})

def profilo(request):
    if request.user.is_authenticated:
        context ={'name': request.user.username}
        return render(request,'Profilo/profilo.html',context=context)
    else:
        redirect("Pagina_generale")

def uscire_profilo(request):
    auth.logout(request)
    return redirect('Pagina_generale')