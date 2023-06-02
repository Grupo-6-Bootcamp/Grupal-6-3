from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def clients(request):
    clientes = [
        {
            "id": 1,
            "nombre": "Diego",
            "apellido": "Herrera",
            "email": "diego.herrer@email.cl",
            "edad": 25,
            "telefono": "31245698"
        },
        {
            "id": 2,
            "nombre": "Nicolas",
            "apellido": "Castro",
            "email": "nico.castro@email.cl",
            "edad": 28,
            "telefono": "31245864"
        },
        {
            "id": 3,
            "nombre": "Carolina",
            "apellido": "Vargas",
            "email": "caro.vargas@email.cl",
            "edad": 35,
            "telefono": "31663864"
        },
        {
            "id": 4,
            "nombre": "Valentina",
            "apellido": "Fernandez",
            "email": "vale.fer@email.cl",
            "edad": 30,
            "telefono": "2654815"
        },
        {
            "id": 5,
            "nombre": "Sebastian",
            "apellido": "Lopez",
            "email": "seba.lopez@mail.cl",
            "edad": 28,
            "telefono": "91856864"
        }
    ]
    return render(request, "clients.html", {"clientes": clientes})

