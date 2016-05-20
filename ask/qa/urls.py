from django.conf.urls import include, url

from . import views

urlpatterns = [

    url(r'^$', views.mainPage),
    url(r'^login/.*$', views.test),
    url(r'^signup/.*$', views.test),
    url(r'^question/(?P<id>[0-9]+)/$', views.questionPage),
    url(r'^ask/.*$', views.test),
    url(r'^popular/.*$', views.popularPage),
	url(r'^new/.*$', views.test)
]