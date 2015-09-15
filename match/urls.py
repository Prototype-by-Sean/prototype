# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns('',
    #url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^test/$', search_view),
    url(r'^$', base_view),
    url(r'^echo$', echo),
)
