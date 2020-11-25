from django.shortcuts import render

# Create your views here.
def fn_facebook(request): 
    return render(request,'facebook.html')
def fn_fb(request):
    return render(request,'facebook-page1.html')     
