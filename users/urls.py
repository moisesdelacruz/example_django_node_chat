from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^@(?P<slug>[-\w]+)/$', views.UserDetailView.as_view(), name='detail'),
    url(r'^profile/$', views.ProfileTemplateView.as_view(), name='profile'),
    url(r'^profile/edit/$', views.ProfileUpdateView.as_view(), name='profile_edit'),
]
