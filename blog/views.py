<<<<<<< HEAD
from django.shortcuts import get_object_or_404, render
=======
from django.shortcuts import render
>>>>>>> 077e043e98c2e6964d96bb90fe3f0e59a5e4307f
from .models import Blog_Entries

def blog(request):
    entry = Blog_Entries.objects.order_by('-pub_date')
    context = {'entry': entry}
    return render(request, 'blog/blog.html', context)
<<<<<<< HEAD

def blog_details(request, blog_id):
    entry = get_object_or_404(Blog_Entries, pk = blog_id)
    context = {'entry': entry}
    return render(request, 'blog/blog_detail.html', context)
=======
>>>>>>> 077e043e98c2e6964d96bb90fe3f0e59a5e4307f
