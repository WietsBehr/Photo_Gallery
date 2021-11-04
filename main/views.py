from django.shortcuts import render
from main.models import users
from django.http import HttpResponse

def index(response):
    return render(response, "main/base.html", {})

def login(response):
    return render(response, "main/login.html", {})

def register(response):
    # if response.method == "POST":
    #     form = users(response.POST)
    #     form.save()
    return render(response, "main/register.html")

def test(response):
    return render(response, "main/test.html", {})


def SAVEDATA(r):
   try:
       name = r.POST['NAME']
       email = r.POST['EMAIL']
       password = r.POST['PASS']

   except:
       return render(r, "main/err.html", {'err': "finding post data"})

#todo: save data to database

   return render(r, "main/SAVEDATA.html", {'name':name})



# def postData(request):
#     name = users({{form}})