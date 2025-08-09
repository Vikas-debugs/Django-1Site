from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.
def home(request):
    ap=Post.objects.all

    return render(request,'myapp/home.html',{'ap':ap})
def about(request):
    return render(request,'myapp/about.html')

def dashboard(request):
    return render(request,'myapp/dashboard.html')
def contact(request):
    return render(request,'myapp/contact.html')
def signuppage(request):
    if request.method == "POST":
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('thank')
    else:
        f = UserCreationForm()



    return render(request,'myapp/signuppage.html',{'f': f})
def loginpage(request):
    if request.method == 'POST':
        f = AuthenticationForm(request, data=request.POST)
        if f.is_valid():
            un = f.cleaned_data.get('username')
            pd = f.cleaned_data.get('password')
            m = authenticate(username=un, password=pd)
            if m is not None:
                login(request, m)
                return redirect('dashboard')
    else:
        f = AuthenticationForm()
    return render(request, 'myapp/loginpage.html', {'f': f})

def readmore(request,blog_id):
    n = get_object_or_404(Post, id=blog_id)
    return render(request,'myapp/readmore.html',{'n': n})
def thank(request):
    return render(request,'myapp/thank.html')
def logoutpage(request):
    logout(request)
    return redirect('/')

def add_blog(request):

    return render(request, 'myapp/add_blog.html')