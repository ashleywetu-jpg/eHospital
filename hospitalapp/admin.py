from django.contrib import admin
from hospitalapp.models import *
from hospitalapp.models import Transaction




# Register your models here.
admin.site.register(Mypatients)

admin.site.register(Mydoctors)

admin.site.register(Myappointments)

admin.site.register(Transaction)


