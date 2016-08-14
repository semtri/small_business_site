'''
Created on 2016. 8. 7.

@author: dennis
'''

from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import AppInfoExtension

class AppInfoExtensionAdmin(PageExtensionAdmin):
    pass


admin.site.register(AppInfoExtension, AppInfoExtensionAdmin)