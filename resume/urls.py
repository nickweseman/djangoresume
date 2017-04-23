from django.conf.urls import url
from resume import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
]