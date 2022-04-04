# 子应用路由分发
from django.urls import path, re_path
from book.views import *
from book.webviews.LoginView import LoginView

urlpatterns = [
    re_path(r'^$', index),
    re_path(r'^booklist/$', booklist),
    re_path(r'^rec/$', receive),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
]
