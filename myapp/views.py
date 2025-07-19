from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def home(request):
    ap=Post.objects.all

    return render(request,'myapp/home.html',{'ap':ap})
def about(request):
    return render(request,'myapp/about.html')
def services(request):
    return render(request,'myapp/services.html')
def languages(request):
    return render(request,'myapp/languages.html')
def contact(request):
    return render(request,'myapp/contact.html')
def signuppage(request):
    return render(request,'myapp/signuppage.html')
def loginpage(request):
    return render(request,'myapp/loginpage.html')
def readmore(request,blog_id):
    n = get_object_or_404(Post, id=blog_id)
    return render(request,'myapp/readmore.html',{'n': n})
