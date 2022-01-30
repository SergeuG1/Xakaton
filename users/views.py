from email import message
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings


def send_email(request):
    if request.method == 'POST':
        try:
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            email = request.POST.get("email")
            email = email.replace('\'', " ").replace(' ','').strip('][').split(',')
            
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=list(email)) 
    
            return redirect("/admin/")
        except Exception as e:    
            return HttpResponseBadRequest(f"<h2>{e.args}</h2>")



