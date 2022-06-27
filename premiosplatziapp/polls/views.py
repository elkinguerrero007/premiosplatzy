from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Estas en la pagina principa de premios platzy")

def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta numero {question_id}")

def result(request, question_id):
    return HttpResponse(f"Estas viendo los resultado de la pregunta numero {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando la pregunta numero {question_id}")



