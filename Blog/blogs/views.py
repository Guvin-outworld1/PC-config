from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from .forms import *


def index(request) -> HttpResponse:
    return render(request, "blogs/index.html")


@login_required
def blog_articles(request) -> HttpResponse:
    """显示所有的博文"""
    blogs = BlogArticle.objects.order_by("date_added")
    context = {"blogs": blogs}
    return render(request, "blogs/blog_articles.html", context)


@login_required
def new_blog(request, blogger_id) -> HttpResponse:
    """添加新博文"""
    blogger = Blogger.objects.get(id=blogger_id)
    if request.method != "POST":
        # 未提交数据：创建一个新表单
        form = BlogForm()
    else:
        # POST提交的数据，对数据进行处理
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.blogger = blogger
            new_blog.save()
            return redirect("blogs:blog_articles")

    context = {"blogger": blogger, "form": form}
    return render(request, "blogs/new_blog.html", context)


@login_required
def edit_blog(request, blog_id) -> HttpResponse:
    """编辑博文"""
    blog = BlogArticle.objects.get(id=blog_id)
    if request.method != "POST":
        # 初次请求: 使用当前博文填充表单
        form = BlogForm(instance=blog)
    else:
        # POST提交的数据，对数据进行处理
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:blog_articles")

    context = {"blogger": blog.blogger, "form": form, "blog": blog}
    return render(request, "blogs/edit_blog.html", context)


@login_required
def blogger_info(request, blogger_id) -> HttpResponse:
    """显示博主信息"""
    blogger = Blogger.objects.get(id=blogger_id)
    blogs = blogger.blogarticle_set.order_by("date_added")
    context = {"blogger": blogger, "blogs": blogs}
    return render(request, "blogs/blogger_info.html", context)
