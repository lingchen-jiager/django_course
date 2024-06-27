from django.urls import path,re_path
# from app01.views import article_create,article_detail,phone_judge 使用下一行的引入方式更简洁一些
from . import views

urlpatterns = [
path('create/', views.article_create,name="article_create"),
    path('<int:article_id>/<str:article_title>/', views.article_detail,name="article_detail"),
    path('list/', views.list,name="article_list"),
    re_path(r'^phone/(?P<phone_num>1[3-9]\d{9})/$', views.phone_judge,name="phone_judge"),]