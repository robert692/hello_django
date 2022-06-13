from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(requests, name):
    return HttpResponse(f"Hello {name}")


def soma(requests, param1, param2):
    return HttpResponse(f"A soma entre {param1} e {param2} é {param1 + param2}")


def subtracao(requests, param1, param2):
    return HttpResponse(f"A subtração de {param1} por {param2} é {param1 - param2}")


def multiplicacao(requests, param1, param2):
    return HttpResponse(f"A multiplicação entre {param1} e {param2} é {param1 * param2}")


def divisao(requests, param1, param2):
    return HttpResponse(f"A divisão de {param1} por {param2} é {param1 / param2} ")
