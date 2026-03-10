
from django.contrib import admin
from django.urls import path,include
from hospitalapp.views import showpat

urlpatterns = [
    path('admin/hospitalapp/showpat/', admin.site.admin_view(showpat), name='showpat'),
    path('admin/', admin.site.urls),

    path('', include('hospitalapp.urls')),


]
