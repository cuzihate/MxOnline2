# coding:utf-8
__author__ = 'zhaohu'
__datetime__ = '2017/2/7 17:21'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['name', 'desc', 'org', 'work_years', 'work_company', 'work_position']
    search_fields = ['name', 'desc', 'org', 'work_years', 'work_company', 'work_position']
    list_filter = ['name', 'desc', 'org', 'work_years', 'work_company', 'work_position']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)