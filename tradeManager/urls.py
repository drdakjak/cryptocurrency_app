from django.conf.urls import url

from tradeManager import views

urlpatterns = [
    
    url(r'^$', views.manager, name='manager'),
    url(r'^new_task/$', views.new_task, name='new_task'),
    url(r'^trade_manager/(?P<task_id>[0-9]+)/$', views.trade_manager, name='trade_manager'),
    url(r'^stop_threads/(?P<task_id>[0-9]+)/$', views.stop_threads, name='stop_threads'),
    url(r'^pubticker_history/$', views.pubticker_history, name='pubticker_history'),
    
    url(r'^buy/(?P<task_id>[0-9]+)/$', views.buy, name='buy'),
    url(r'^sell/(?P<task_id>[0-9]+)/$', views.sell, name='sell'),
    url(r'^close/(?P<task_id>[0-9]+)/(?P<trade_id>[0-9]+)/$', views.close, name='close'),
]