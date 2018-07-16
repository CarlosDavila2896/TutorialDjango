from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^alumnos/(?P<nivel>[1-9]+)/$', views.Alumno_list),
]
