from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'(?P<id>[0-9]\w*)', views.detail, name='detail'),
    #url(r'(?P<num>[0-9]\w*)', views.sam, name='sam'),

    url(r'(?P<id>[0-9]\w*)', views.blank, name='blank'),
]
# r'^(?P<compu>[+&\w-]+)$'
# path('articles/<int:year>/', views.year_archive),
