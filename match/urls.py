# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url, include
import views
from views import *

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^test/$', SearchView),
)
