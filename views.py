'''
Created on 2016. 8. 15.

@author: dennis
'''

from django.http.response import HttpResponse
from django.shortcuts import render


def contact_us(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}
        
        return HttpResponse(
                            )
    else:
        return HttpResponse()
    

def login_dlg(request):
    return render(request, "login_dlg.tmpl.html", {})