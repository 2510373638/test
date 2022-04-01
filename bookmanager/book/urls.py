# 子应用路由分发
from django.urls import path, re_path
from book.views import *

urlpatterns = [
    re_path(r'^$',index),
]