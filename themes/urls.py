from django.conf.urls import url
# views
from themes import views

urlpatterns = [
    url(r'^$', views.ThemeListView.as_view(), name='list'),
    url(r'^(?P<pk>[-\ \w]+)/detail/$', views.ThemeDetailView.as_view(), name='detail'),
]
