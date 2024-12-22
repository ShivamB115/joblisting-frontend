from django.contrib import admin
from django.urls import path, include
from jobs.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jobs.urls')),
    path('',index),
]
