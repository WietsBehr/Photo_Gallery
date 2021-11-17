from django.contrib import admin
from .models import users
from .models import photos

admin.site.register(users)
admin.site.register(photos)
# Register your models here.
