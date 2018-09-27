from django.shortcuts import render

def index(request):
    return render(reqeust, "blog/blog.html")
