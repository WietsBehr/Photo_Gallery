from django.shortcuts import render
from main.models import users
from passlib.hash import sha256_crypt
from django.http import HttpResponse


def index(response):
    return render(response, "main/base.html", {})

def login(r):
    if r.method == "POST":

        try:

            email = r.POST['email']
            password = r.POST['password']
            row = users.objects.get(email=email)
            password_hash =  row.password
            if ( sha256_crypt.verify(password,password_hash)):
                params = {'name' : row.username}
                return render(r, "main/gallery.html", params)
            else:
                return render(r, "main/BannerERR.html", {'msg': "Password incorrect!"})

        except:
            return render(r, "main/BannerERR.html", {'msg': "User not found, please register!"})
    else:
        return render(r, "main/login.html", {})


def register(r):
    if (r.method == "POST"):
        try:
            name = r.POST['NAME']
            email = r.POST['EMAIL']
            password = r.POST['PASS']
            password = sha256_crypt.encrypt(password)

        except:
            return render(r, "main/register.html", {})

            # todo: check if user key exist
        users.objects.create(username=name, email=email, password=password)

        return render(r, "main/login.html", {'name': name})
    else:
        return render(r, "main/register.html", {})

def test(response):
    return render(response, "main/test.html", {})







# def postData(request):
#     name = users({{form}})