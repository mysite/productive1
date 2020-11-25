
from django.shortcuts import get_object_or_404, render
from .models import Blog_Entries

def blog(request):
    entry = Blog_Entries.objects.order_by('-pub_date')
    context = {'entry': entry}
    return render(request, 'blog/blog.html', context)

def blog_details(request, blog_id):
    entry = get_object_or_404(Blog_Entries, pk = blog_id)
    context = {'entry': entry}
    return render(request, 'blog/blog_detail.html', context)
