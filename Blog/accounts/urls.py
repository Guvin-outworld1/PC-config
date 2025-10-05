from django.urls import path, include
from . import views

app_name = "accounts"
urlpatterns = [
    # 将auth.urls直接包含到urlpatterns中，不使用空路径
    path('login/', include('django.contrib.auth.urls')),
    # 注册页面
    path("register/", views.register, name="register"),
]

