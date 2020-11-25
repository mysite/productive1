# Create your views here.
from django.shortcuts import render
from django.views.generic import FormView
from django.shortcuts import redirect
<<<<<<< HEAD
from .models import Contact, Newsletter #, Pictures
=======
from .models import Contact #, Pictures
>>>>>>> 077e043e98c2e6964d96bb90fe3f0e59a5e4307f
from .forms import UploadPicture
#from django.core.urlresolvers import reverse_lazy
#from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    #picture = Pictures.objects.filter(presentation ="yes")
    #picture = Pictures.objects.order_by('-pub_date')
    #picture = Pictures.objects.filter(category = 1)
    #context = {'picture': picture}
    #return render(request, 'polls/index.html', context)
    return render(request, 'polls/index.html')

def joelette(request):
    return render(request, 'polls/joelette.html')

def ueber_uns(request):
    return render(request, 'polls/ueber_uns.html')

def impressum(request):
    return render(request, 'polls/impressum.html')

def dsgvo(request):
    return render(request, 'polls/dsgvo.html')

<<<<<<< HEAD
=======
#class upload(FormView):
#    template_name = 'polls/upload.html'
#    form_class = UploadPicture

#    def form_valid(self, form):
#        profile_image = Pictures(
#           image=self.get_form_kwargs().get('files')['image'])
#        profile_image.save()
#        return redirect('/pictures')

#def contact(request):
#    return render(request, 'polls/contact.html')

>>>>>>> 077e043e98c2e6964d96bb90fe3f0e59a5e4307f
def contact(request):
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('email') and request.POST.get('subject') and request.POST.get('text'):
                post=Contact()
                post.name= request.POST.get('name')
                post.email= request.POST.get('email')
                post.subject= request.POST.get('subject')
                post.text= request.POST.get('text')
                post.save()
                
                return render(request, 'polls/contact_submit.html')  
<<<<<<< HEAD
        else:
                return render(request,'polls/contact.html')

def newsletter(request):
        if request.method == 'POST':
            if request.POST.get('email'):
                post=Newsletter()
                post.email= request.POST.get('email')
                post.save()
                
                return render(request, 'polls/contact_submit.html')  
        else:
                return render(request,'polls/newsletter.html')

def gruende(request):
    return render(request, 'polls/gruende.html')

def fragen(request):
    return render(request, 'polls/fragen.html')

#class upload(FormView):
#    template_name = 'polls/upload.html'
#    form_class = UploadPicture

#    def form_valid(self, form):
#        profile_image = Pictures(
#           image=self.get_form_kwargs().get('files')['image'])
#        profile_image.save()
#        return redirect('/pictures')

#def contact(request):
#    return render(request, 'polls/contact.html')
=======

        else:
                return render(request,'polls/contact.html')
>>>>>>> 077e043e98c2e6964d96bb90fe3f0e59a5e4307f
