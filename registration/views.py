from django.shortcuts import render

def index(request):
    return render(request, "land.html")

def login(request):
    return render(request, "login.html")

