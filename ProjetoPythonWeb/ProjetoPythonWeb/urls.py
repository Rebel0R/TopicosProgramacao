"""ProjetoPythonWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appPythonWeb.views import home, formulario, inserir, visualizar, editar, updateBD, excluir

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('formulario/', formulario, name='formulario'),
    path('inserir/', inserir, name='inserir'),
    path('visualizar/<int:pk>/', visualizar, name='visualizar'),
    path('editar/<int:pk>/', editar, name='editar'),
    path('updateBD/<int:pk>/', updateBD, name='updateBD'),
    path('excluir/<int:pk>/', excluir, name='excluir'),
]
