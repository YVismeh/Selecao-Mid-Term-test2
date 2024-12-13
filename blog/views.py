from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog
# Create your views here.

def blog(request, **kwargs):
    if kwargs.get("category"):
        blog = Blog.objects.filter(category__title=kwargs.get("category"))
    else:
        blog = Blog.objects.all()
        
    blog_paginate = Paginator(blog, 1)
    first_page = 1
    last_page = blog_paginate.num_pages

    try:
        page_number = request.GET.get("page")
        blog = blog_paginate.get_page(page_number)
    except:
        page_number = first_page
        blog = blog_paginate.get_page(first_page)
    
    context = {
        "blogs":blog,
        "first" : first_page,
        "last" : last_page
    }


    return render(request, 'blog/blog.html', context=context)    









def blog_details(request):
    return render(request, 'blog/blog-details.html')