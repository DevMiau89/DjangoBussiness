from django.conf.urls import url
from django.contrib import admin

from . views import (
    index,
    about,
    services,
    portfolio,
    portfolio_detail,
    blog,
    post_detail,
    faq,
    contact
)

urlpatterns = [
    url(r'^$', index),
    url(r'^about/$', about),
    url(r'^services/$', services),
    url(r'^portfolio/$', portfolio),
    url(r'^blog/$', blog),
    url(r'^blog/(?P<id>\d+)/$', post_detail),
    url(r'^portfolio/(?P<id>\d+)/$', portfolio_detail),
    url(r'^faq/$', faq),
    url(r'^contact/$', contact),
]
