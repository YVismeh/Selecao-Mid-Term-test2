from django.urls import path
from .views import blog, blog_details


app_name = "blog"

urlpatterns = [
    path("", blog, name="blog"),
    path("category/<str:category>", blog, name="blog-category"),
    path("blog-details/", blog_details, name="blog-details"),
]