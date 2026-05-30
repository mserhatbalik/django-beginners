from django.shortcuts import render


# Create your views here.
def home_page_view(request):
    context = {"description": "This is our glorious Company Website"}
    return render(request, "home.html", context)
