# encoding: utf-8
'''

'''

from django.conf.urls import url
from django.contrib.staticfiles.views import serve


urlpatterns = [
      url(r'^.*$', serve, kwargs={'path': '/armylist/index.html',}, name='index'),
]
