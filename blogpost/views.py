from django.shortcuts import render
from .models import blogpost
from django.contrib import messages
# Create your views here.


def blogposts(request):
   search =request.GET.get('search')
  
   
  
   if search and len(search)<100:
      
      blog=blogpost.objects.filter(blogname__icontains=search)
      blog=blogpost.objects.filter(blogtitle__icontains=search)
      blog=blogpost.objects.filter(text__icontains=search)
      messages.success(request, 'Search results for '+search +' are......')
      return render(request,'blog/blogpost.html',{'blog':blog}) 
   
   blog=blogpost.objects.all()
   return render(request,'blog/blogpost.html',{'blog':blog }) 
  #else:
    #  return render(request,'blog/blogpost.html',{'blog':blog})
def blogpage(request,slug):
    id=slug
    blog=blogpost.objects.filter(id=id)
    return render(request,'blog/blogpage.html', {'blog':blog}) 
def blogcomment():
      comment=request.POST.get('comment')
      email=request.POST.get('email')
      number=request.POST.get('number')
      subject=request.POST.get('subject')
      quary1=request.POST.get('quary1')
   