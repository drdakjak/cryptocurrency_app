from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$',include('tradeManager.urls',namespace='base')),
    url(r'^manager/', include('tradeManager.urls',namespace='manager')),
    url(r'^admin/', include(admin.site.urls)),
)
