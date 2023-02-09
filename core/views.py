from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, a: int, b: int):
    return HttpResponse('<h1>A soma de {} + {} é {}</h1>'.format(a, b, a + b))

def subtracao(request, a: int, b: int):
    return HttpResponse('<h1>A subtração de {} - {} é {}</h1>'.format(a, b, a - b))

def multiplicacao(request, a: int, b: int):
    return HttpResponse('<h1>A multiplicação entre {} X {} é {}</h1>'.format(a, b, (a * b)))

def divisao(request, a: int, b: int):
    return HttpResponse('<h1>A divisão entre {} / {} é {}</h1>'.format(a, b, (a / b)))