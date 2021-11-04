from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return render(response, "main/base.html", {})

def login(response):
    return render(response, "main/login.html", {})

def register(response):
    return render(response, "main/register.html", {})

def test(response):
    return render(response, "main/test.html", {})

