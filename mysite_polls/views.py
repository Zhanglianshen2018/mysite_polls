from django.http import HttpResponse


def home(request):
    return HttpResponse("欢迎访问我的网站")