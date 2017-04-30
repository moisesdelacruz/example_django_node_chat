from django.conf.urls import url
# views
from themes import views

urlpatterns = [
    url(r'^$', views.ThemeListView.as_view(), name='list'),
    url(r'^theme/new$', views.ThemeCreateView.as_view(), name='create'),
    url(r'^theme/(?P<pk>[-\ \w]+)/$', views.ThemeDetailView.as_view(), name='detail'),
    url(r'^theme/(?P<pk>[-\ \w]+)/update/$', views.ThemeUpdateView.as_view(), name='update'),
]
