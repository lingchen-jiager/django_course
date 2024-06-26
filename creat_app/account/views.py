from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
# def login(request):
#     html = '''
#     <form >
#     <input name="username">
#     </form>
# #     '''  一般不这样写，随着网页复杂度的提高，这个html会越来越大，所以我们一般采用template模板的形式来实现,通过render函数引入html文件。。
#     return HttpResponse(html)



# def test(request):
#
#
#     return HttpResponse("this is a get request.")


def login(request):

    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        return HttpResponse(f"用户{username}的密码是{password}。")
    elif request.method == "GET":
        forbiden_ip = ["127.0.0.1"]
        print(request.META.get('HTTP_USER_AGENT')) #使用request.META.get('') 获取所有的参数，根据返回结果查看参数
        # if request.META.get('REMOTE_ADDR') in forbiden_ip :  #当请求此网址的客户端ip在禁止列表时，返回ip禁用提示。
        #     return HttpResponse("ip被禁用，请求异常")
        if 'python' in request.META.get('HTTP_USER_AGENT'): #当检测到user agent为python时，返回禁用爬虫提示。
            return HttpResponse("禁止爬虫")  #当然这个判断需要使用python爬虫使用get爬取此网址（127.0.0.1：8000/account/login），且未使用user agent伪装的条件下才能起效。


        return render(request,"index.html")






class RegisterView(View):
    def get(self,request):
        return render(request,"register.html")
    def post(self,request):
        username = request.POST.get("username")

        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        return HttpResponse(f"用户{username}密码是{password}")


