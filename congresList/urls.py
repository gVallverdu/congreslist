from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.congres_list, name='congres_list'),
    url(r"^new/$", views.new_congre, name="new_congre"),
    url(r"^edit/(?P<pk>\d+)$", views.edit_congre, name="edit_congre"),
]
