from blog.models import CategoryBlog

def general_context(request):
    context = {
        'categories' : CategoryBlog.objects.all(),
    }
    return context