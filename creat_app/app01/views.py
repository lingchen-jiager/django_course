from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse("hello world")
def article_create(request):

    return HttpResponse("创建一篇新文章")

def article_detail(request,article_id,article_title): # article_id是urls.py中定义路由时的name
    return HttpResponse(f"这篇文章的id是{article_id},<br>title是{article_title}")

def phone_judge(request,phone_num): # article_id是urls.py中定义路由时的name
    return HttpResponse(f"手机号是{phone_num}")