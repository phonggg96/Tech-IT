from home.views import index, login_view
from django.conf.urls import url
from . import views
app_name = 'home'

urlpatterns = [
     url(r'^$', views.index, name ='index'),
     url(r'^login/', login_view, name='login'),
     url(r'^home/(?P<id>\d+)/$', views.contact, name='contact'),
     url(r'^add-comment/$', views.add_comment, name='new-comment'),
     url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.Category, name='category'),
]