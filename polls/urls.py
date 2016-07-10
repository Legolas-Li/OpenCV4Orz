from django.conf.urls import url,include,patterns
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index' ),
    url(r'^process/',views.process, name='process' ),
]