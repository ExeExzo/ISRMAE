from django.contrib import admin
from django.urls import path, include
from main import views
from voen_chas import views

urlpatterns = [
    path('', include('main.urls')),
    path('', include('voen_chas.urls')),
    path('', admin.site.urls, name='admin'),
]

admin.site.index_title = "ИС УВАТ"
admin.site.site_header = "IS UVAT"
admin.site.site_title = "IS UVAT"

