from django.contrib import admin

# Register your models here.
from .models import items
from .models import Guser

admin.site.register(Guser)
admin.site.register(items)

