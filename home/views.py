from django.shortcuts import render
from django.http import HttpResponse
from home.views import *

def index(request):
    Np = [
        {'name' : 'abhijeet Gupta', 'age': '26'},
        {'name' : 'Rohan Sharma', 'age': '23'},
        {'name' : 'Vicky Kaushal', 'age': '24'},
        {'name' : 'Saudeep', 'age': '17'},
        {'name' : 'Rahul Rahi', 'age': '15'}, 
    ]
    
    vagetable = ['pumkin', 'alu', 'begun ']
    
    

    
    return render(request, "index.html", context= {'Np': Np, 'vagetable': vagetable, })
  
  
def about(request):
    return HttpResponse("Welcome To About Page")
    
def contact(request):
    return HttpResponse("Welcome To Contact Page")

