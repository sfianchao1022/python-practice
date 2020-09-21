from products import views
from django.urls import path

urlpatterns = [
    path('', views.index),  # products的主畫面
    path('new', views.new),  # products/new的頁面 呼叫views的new函式(不需要加括弧)來顯示new頁面

]
