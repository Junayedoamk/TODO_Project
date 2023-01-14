from django.contrib import admin
from .models import User, TODO

# Register your models here.

admin.site.register(User)
admin.site.register(TODO)