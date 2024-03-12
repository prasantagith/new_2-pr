from django.http import HttpResponse

def project(requset):
    return HttpResponse(" hello world")

def auto(requset):
    return HttpResponse("good too restart")
   