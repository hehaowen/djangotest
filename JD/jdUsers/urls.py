from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^regist/', regist, name='regist'),
    url(r'^regist_henld/', regist_henld, name='regist_henld'),
    url(r'^login_hanle/', login_hanle, name='login_hanle'),
    url(r'^order/', order, name='order'),
    url(r'^user/', user, name='user'),
]
