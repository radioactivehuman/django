from django.shortcuts import render,HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages
# Create your views here.


# main
def home(request):
    return render(request,"home.html")


# database
def contact(request):
    if request.method == 'POST':
     email = request.POST.get('email')
     name = request.POST.get('name')
     country = request.POST.get('country')
     massage = request.POST.get('massage')
     s=Contact(email=email,name=name,country=country,massage=massage)
     s.save()
     msg=messages.success(request, 'message received thank you for your response.')
    

     return render(request,"contact.html")

    return render(request,"contact.html")


# information about page
def about(request):
    return render(request,"about.html")

def privicy(request):
    return render(request,"privicy.html")

def disclamer(request):
    return render(request,"disclamer.html")

# search function 
def search(request):
    query=request.GET['query']
    if len(query)>78 or len(query)==0:
        allPosts=Post.objects.none()
    else:
     allPosts= Post.objects.filter(title__icontains=query)
    if allPosts.count()==0:
      messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts,'query': query}
    return render(request, 'search.html',params)

     

# content type 

def hacking(request):
     posttech=Post.objects.filter(category="hacking")
     t={"posttech":posttech}
     return render(request,"hacking.html",t)

def myst(request):
     posttech=Post.objects.filter(category="myst")
     t={"posttech":posttech}
     return render(request,"myst.html",t)

def tech(request):
     posttech=Post.objects.filter(category="tech")
     t={"posttech":posttech}
     return render (request,'tech.html',t)
     

def business(request):
    posttech=Post.objects.filter(category="business")
    t={"posttech":posttech}
    return render(request,"business.html",t)

def other(request):
    posttech=Post.objects.filter(category="other")
    t={"posttech":posttech}
    return render(request,"other.html",t)









