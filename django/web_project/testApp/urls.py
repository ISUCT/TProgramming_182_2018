from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns



i18n_urls = (
    url(r'^$', views.home, name="home")
    # path('text/', views.hello_there, name="text")
)