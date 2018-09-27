from django.shortcuts import render

def index(request):
    return render(request, "personal/home.html")

def contact(request):
    return render(request, "personal/contacts.html", {"content": ['If you want o contact me, connect to email', 'some@example.com`']})
