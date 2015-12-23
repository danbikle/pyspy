from django.conf.urls import url

from . import views
app_name = 'pyspy'
urlpatterns = [
    # ex: /pyspy/
    url(r'^$', views.index, name='index'),
]

