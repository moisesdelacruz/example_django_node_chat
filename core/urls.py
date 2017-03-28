from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^node_api$', views.node_api, name='node_api'),
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}, name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
]
