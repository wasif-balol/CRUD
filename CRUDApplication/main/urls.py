from django.conf.urls import url
from . import views


app_name='main'
urlpatterns = [
    url(r'^create/$', views.Create.as_view(), name='create'),
    url(r'^(?P<pk>\d+)$', views.Details.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', views.Update.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.Delete.as_view(), name='delete'),
    url(r'', views.UsersList.as_view(), name='allUsers'),
]