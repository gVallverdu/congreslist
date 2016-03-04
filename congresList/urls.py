from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.congres_list, name='congres_list'),
]
