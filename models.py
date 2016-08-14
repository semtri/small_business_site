'''
Created on 2016. 8. 7.

@author: dennis
'''

from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class AppInfoExtension(PageExtension):
    feature_image = models.ImageField(null=True, upload_to='features')
    apple_store_id = models.CharField(null=True, max_length=256)
    google_store_id = models.CharField(null=True, max_length=256)
    
extension_pool.register(AppInfoExtension)