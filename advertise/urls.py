"""advertise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from myappl import views
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^(?P<id>\d+)/$',views.post_detail,name='details'),
    url(r'^register/',views.register,name='signup'),
    url(r'^post/',views.post_ads,name='post'),
    url(r'^logout/', views.log_out, name='logout'),
    url(r'^base/', views.dashboard, name='base'),
    url(r'^ads/', views.ads, name='ads'),
    url(r'^category/(?P<category_slug>[\w-]+)/$',views.category, name='category'),
    url(r'^create_profile',views.create,name='create'),
    url(r'^register_suc', views.register_suc, name='succ'),
    url(r'^edit_profile',views.profile_edit,name='profile_edit'),
    url(r'^password_reset', views.reset_password, name='pass_reset'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^about/',views.about,name='about'),
    url(r'^api/',include('myappl.api.urls',namespace='api')),
    #url(r'^api/ads/',CatListView.as_view(),name='ads_list'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
