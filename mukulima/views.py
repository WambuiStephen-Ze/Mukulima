from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

# def blog-details(request):
#     return render(request, 'blog-details.html')

def services(request):
    return render(request, 'services.html')

def testimonials(request):
    return render(request, 'testimonials.html')

