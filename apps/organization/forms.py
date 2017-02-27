# coding:utf-8
__author__ = 'zhaohu'
__datetime__ = '2017/2/24 14:59'

import re
from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号是否合法，必须以clean_开头
        :return:
        """
        moblie = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}|^17[06]\d{8}"
        p = re.compile(REGEX_MOBILE)
        if p.match(moblie):
            return moblie
        else:
            raise forms.ValidationError(u'手机号码非法', code='mobile_invalid')
