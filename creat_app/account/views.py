from django.shortcuts import render
from django.http import HttpResponse
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

    return render(request,"index.html")