from django.shortcuts import render

# Create your views here.

exes = [{
    "title" : "sitting"
    },
    {
        "title" : "workout"
    }
    ]

def  home(request):
    context = {
        "exes" : exes
    }
    return render(request, "exercise/home.html", context )

def about(request):
    return render(request, "exercise/about.html", {"page_title" : "About"})