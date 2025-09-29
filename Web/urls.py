
    from django.contrib import admin
    from django.urls import path
    from sitoWeb import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',views.Pagina_generale, name='Pagina_generale'),
        path('registrazione/',views.Pagina_registrazione , name='Pagina_registrazione'),
        path('accesso/',views.Acceso_account,name='Accesso'),
        path('profilo/',views.profilo,name='Profilo'),
        path('uscire/',views.uscire_profilo,name='Uscire_Profilo'),
    ]   
