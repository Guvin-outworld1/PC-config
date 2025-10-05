from django.urls import path

from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.index, name="index"),
    path("blog_articles/", views.blog_articles, name="blog_articles"),
    path("blogger_info/<int:blogger_id>/", views.blogger_info, name="blogger_info"),
    path("new_blog/<int:blogger_id>/", views.new_blog, name="new_blog"),
    path("edit_blog/<int:blog_id>/", views.edit_blog, name="edit_blog"),  
]
