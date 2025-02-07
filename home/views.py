from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    peoples = [
        {'name':'Abhijeet Gupta','age':26},
        {'name':'Rohit Sharma','age':17},
        {'name':'Vicky Kaushal','age':24},
        {'name':'Deepanshu Chaurasiya','age':15},
        {'name':'Sandeep','age':63}
    ]

    vegetables = ['pumpkin','tomato','potato']

    context={'page':'contact'}

    return render(request, "home/index.html",context={'peoples':peoples,'vegetables':vegetables,'page':'home'})

def about(request):
    context={'page':'About'}
    return render(request, "home/about.html",context)

def contact(request):
    context={'page':'contact'}
    return render(request, "home/contact.html",context)

def success_page(request):
    return HttpResponse("<h1>Hey this is a success page.</h1>")