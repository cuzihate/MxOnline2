# coding:utf-8
__author__ = 'zhaohu'
__datetime__ = '2017/2/7 16:41'


import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner, UserProfile


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '虎哥哥的小木屋'
    site_footer = '虎哥在线'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


class UserProfileAdmin(object):
    list_display = ['nick_name', 'birday', 'gender', 'mobile', 'email']
    search_fields = ['nick_name', 'birday', 'gender', 'mobile']
    list_filter = ['nick_name', 'birday', 'gender', 'mobile']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(UserProfile, UserProfileAdmin)