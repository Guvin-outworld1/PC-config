"""为应用程序accounts定义URL模式"""
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # 包含默认身份验证的URL模式
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
