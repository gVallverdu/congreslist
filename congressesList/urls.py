from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.congresses_list, name='congresses_list'),
    url(r"^new/$", views.new_congress, name="new_congress"),
    url(r'^congress/(?P<congress_id>\d+)/$', views.congress_detail, name='congress_detail'),
    url(r"^edit/(?P<congress_id>\d+)$", views.edit_congress, name="edit_congress"),
]
