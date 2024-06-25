from django.urls import path,re_path
from app01.views import article_create,article_detail,phone_judge


urlpatterns = [
path('create/', article_create,name="article_create"),
    path('<int:article_id>/<str:article_title>/', article_detail,name="article_detail"),
    re_path(r'^phone/(?P<phone_num>1[3-9]\d{9})/$', phone_judge,name="phone_judge"),]