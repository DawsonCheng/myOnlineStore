#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from netstoreapp import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),#主页
    url(r'^login/',views.userlogin,name='login'),#登陆
    url(r'^register/',views.register,name='register'),#注册
    url(r'^chdata/',views.chdata,name='chdata'),#修改资料
    url(r'^chpwd/',views.chpwd,name='chpwd'),#修改密码
    url(r'^cart/',views.cart,name='cart'),#购物车
    url(r'^mydata/',views.mydata,name='mydata'),#我
    url(r'^commodity/',views.commodity,name='commodity'),#商品页\
    url(r'^logout/',views.user_logout,name='logout'),#注销
    url(r'^classify/',views.classify,name='classify'),
    url(r'^add/',views.add,name='add'),
    url(r'^iframe/',views.iframe,name='iframe'),
    url(r'^cart_add/',views.cart_add,name='cart_add'),
)
