'''
Created on 2016. 8. 7.

@author: dennis
'''

from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import AppInfoExtension, ContactUs

class AppInfoExtensionAdmin(PageExtensionAdmin):
    pass


admin.site.register(AppInfoExtension, AppInfoExtensionAdmin)

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('category', 'email', 'received')


admin.site.register(ContactUs, ContactUsAdmin)