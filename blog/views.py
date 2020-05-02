from django.shortcuts import render
from .models import Blog_Entries

def blog(request):
    entry = Blog_Entries.objects.order_by('-pub_date')
    context = {'entry': entry}
    return render(request, 'blog/blog.html', context)
