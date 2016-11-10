'''
Created on 2016. 8. 15.

@author: dennis
'''

import datetime
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import ContactUs

def contact_us(request):
    if request.method == 'POST':
        contactUs = ContactUs()
        
        contactUs.category = request.POST.get('category')
        contactUs.name = request.POST.get('name')
        contactUs.phone = request.POST.get('phone')
        contactUs.email = request.POST.get('email')
        contactUs.message = request.POST.get('message')
        contactUs.received = datetime.datetime.now()
        contactUs.save();
        
        return HttpResponse(
                            )
    else:
        return HttpResponse()
    

def login_dlg(request):
    return render(request, "login_dlg.tmpl.html", {})
