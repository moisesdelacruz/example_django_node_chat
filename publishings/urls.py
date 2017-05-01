from django.conf.urls import url
# views
from publishings import views

urlpatterns = [
    url(r'^$', views.PublishingListView.as_view(), name='list'),
    url(r'^publishing/new$', views.PublishingCreateView.as_view(), name='create'),
    url(r'^publishing/(?P<uuid>[^/]+)/$', views.PublishingDetailView.as_view(), name='detail'),
    url(r'^publishing/(?P<uuid>[^/]+)/update/$', views.PublishingUpdateView.as_view(), name='update'),
    url(r'^publishing/(?P<uuid>[^/]+)/delete/$', views.PublishingDeleteView.as_view(), name='delete'),
]
