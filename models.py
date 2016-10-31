'''
Created on 2016. 8. 7.

@author: dennis
'''

from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


def content_file_name(instance, filename):
    return '/'.join(['app_info', str(instance.pk), filename])
        
        
class AppInfoExtension(PageExtension):
    feature_image = models.ImageField(null=True, blank=True, upload_to=content_file_name)
    icon_image = models.ImageField(null=True, blank=True, upload_to=content_file_name)
    apple_store_id = models.CharField(null=True, blank=True, max_length=256)
    google_store_id = models.CharField(null=True, blank=True, max_length=256)
    
    
         
extension_pool.register(AppInfoExtension)