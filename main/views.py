from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render
from main.models import users
from main.models import photos
from passlib.hash import sha256_crypt
from django.http import HttpResponse
from main.forms import ImageForm


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
                params = {'name' : row.username, 'user_id':row.id}
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
            password2 = r.POST['PASS2']
            password = sha256_crypt.encrypt(password)
        except:
            return render(r, "main/register.html", {})

        if (password2 != r.POST['PASS']):
            return render(r, "main/errorRegistration.html", {'msg': "Passwords do not match !" , 'name':name , 'email':email})

        try:
            if (users.objects.get(email=email)):
                return render(r, "main/errorRegistration.html", {'msg': "User already exists!"})
        except:
            users.objects.create(username=name, email=email, password=password)
            return render(r, "main/login.html", {})
    else:
        return render(r, "main/register.html", {})


def test(response):
    return render(response, "main/test.html", {})

# @login_required
def gallery(request, user_id):
    if (request.method == "GET"):
        # user = users.objects.get(id=user_id)
        # images = user.photos_set.objects.all()
        return render(request, "main/upload.html", {'user_id': user_id})
    # images = user.photos_set.objects.all()
    return render(request, "main/gallery.html", {})

# @login_required
# @transaction.atomic
def upload(request, user_id):
    if request.method == 'POST':
        # user_id = request.POST[user]
        form = ImageForm(request.POST, request.FILES, request.POST[user_id], initial={'user_id': user_id})
        # initial = {'users': users}
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'main/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'main/upload.html', {'form': form})