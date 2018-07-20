#!/usr/bin/env python
# -*- coding: utf-8 -*-
# learning_logs子文件的urls
from django.urls import path,re_path
from django.contrib.auth.views import login
from . import views
app_name = 'users'
urlpatterns = [
    path('login/',login,{'template_name':'users/login.html'},
        name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register'),
]
