from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog
# Create your views here.

def blog(request, category=None):
    if category is not None:
        blog = Blog.objects.filter(category__title=category)
        context ={
            'blog': blog
        }
    else:
        blog = Blog.objects.all()
        context ={
            'blog': blog
        }
        
    blog_paginate = Paginator(blog, 2)
    first_page = 1
    last_page = blog_paginate.num_pages

    try:
        page_number = request.GET.get("page")
        blp = blog_paginate.get_page(page_number)
    except:
        page_number = first_page
        blp = blog_paginate.get_page(first_page)
    
    context = {
        "blogs":blp,
        "first" : first_page,
        "last" : last_page
    }


    return render(request, 'blog/blog.html', context=context)    









def blog_details(request, id):
    #id = request.GET.get("id")
    blog = get_object_or_404(Blog, id=id)
    contex = {
        'blog':blog,
    }
    return render(request, 'blog/blog-details.html', context=contex)