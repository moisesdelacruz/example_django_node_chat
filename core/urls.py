from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^node_api$', views.node_api, name='node_api'),
]
