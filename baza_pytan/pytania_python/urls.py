from django.urls import path
from pytania_python import views
from django.views.generic import TemplateView
from pytania_python import views

app_name = 'pytania python'

urlpatterns = [
    path('',TemplateView.as_view(template_name = 'index.html')),
]
