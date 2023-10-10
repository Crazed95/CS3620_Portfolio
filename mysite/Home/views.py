from django.shortcuts import render
from django.http import  HttpResponse
from .models import Hobbie
from .models import Portfolio
from django.template import loader


# Create your views here.
def index(request):
    return  render(request, 'Home/home.html')
def hobbie(request):
    hobbie_list = Hobbie.objects.all()
    #template = loader.get_template('Home/hobbie_index.html')
    context = {
        'hobbie_list': hobbie_list,
    }
    return  render(request, 'Home/hobbie_index.html', context)
def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list':portfolio_list
    }
    return render(request, 'Home/portfolio_index.html', context)
def contact(request):
    return render(request, 'Home/contact.html')
def h_details(request, hobbie_id):
    hobbie = Hobbie.objects.get(pk=hobbie_id)
    context = {
        'hobbie':hobbie,
    }
    return render(request, 'Home/hobbie_details.html', context)
def p_details(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    context = {
        'portfolio': portfolio,
    }
    return  render(request, 'Home/portfolio_details.html', context)
