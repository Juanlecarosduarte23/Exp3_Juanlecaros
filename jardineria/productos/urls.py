from django.urls import path
from .views import index, otra, crear, eliminar, modificar, registrar, mostrar, somos , galeria,contacto, otra2, modificar2, mostrar2

urlpatterns=[ 
    path('', index, name="index"),
    path('somos', somos, name="somos"),
    path('galeria', galeria, name="galeria"),
    path('contacto', contacto, name="contacto"),


    path('otra2', otra2, name="otra2"),

    path('modificar2', modificar2, name="modificar2"),


    path('mostrar2', mostrar2, name="mostrar2"),


    path('otra/', otra, name="otra"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('eliminar2/<id>', eliminar, name="eliminar2"),
    path('modificar/<id>', modificar, name="modificar"),
     path('modificar2/<id>', modificar2, name="modificar2"),
    path('registrar/', registrar, name="registrar"),
    path('mostrar/', mostrar, name="mostrar"),
 
]