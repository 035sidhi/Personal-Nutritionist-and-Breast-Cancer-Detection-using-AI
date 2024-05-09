from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from foodie import settings

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate.html', views.calculate_view, name='calculate'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
