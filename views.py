from django.shortcuts import render

def home(req):
    return render(req , 'app1/home.html')

def about(req):
    return render(req , 'app1/about.html')

def contact(req):
    return render(req , 'app1/contact.html')