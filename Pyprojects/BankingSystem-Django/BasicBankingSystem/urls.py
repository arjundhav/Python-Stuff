
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "MGMs Bank"
admin.site.site_title = "MGMs Bank"
admin.site.index_title = "Welcome to MGMs Bank"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
