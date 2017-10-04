from django.conf.urls import  url,include

from .views import CatListView,CatDetailView,AdsListView,UsersListView,userListView




urlpatterns=[
    url(r'^cat/',CatListView.as_view(),name='cat'),
    url(r'^ads/',AdsListView.as_view(),name='ads'),
    url(r'^User/', UsersListView.as_view(), name='User'),
    url(r'^user/', userListView.as_view(), name='user'),
    url(r'^cat/(?P<id>\d+)/$',CatDetailView.as_view(),name='ads_detail'),
]