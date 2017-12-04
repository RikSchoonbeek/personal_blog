from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_posts, name='show_posts'),
    url(r'^category/(?P<category>[\w-]+)/$', views.show_posts, name='show_by_category'),
]