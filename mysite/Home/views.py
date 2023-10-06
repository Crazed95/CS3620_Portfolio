from django.shortcuts import render
from django.http import  HttpResponse
from .models import Hobbie
from .models import Portfolio
# Create your views here.
def index(request):
    return  HttpResponse('My Name is Nic Cabezas, I am currently working on finishing my CS degree while working full time at  Ogden Technical School. \n'
                         'I Currently work as an IT Senior Tech. I am married and am at the ripe old age of 28')
def hobbie(request):
    hobbie_name = Hobbie.objects.all()
    return  HttpResponse(hobbie_name)
def portfolio(request):
    portfolio_name = Portfolio.objects.all()
    return  HttpResponse(portfolio_name)
def contact(request):
    return  HttpResponse('Student Email: nicolascabezas@mail.weber.edu')