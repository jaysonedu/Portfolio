from django.shortcuts import render

# 7/8 first edit to views
def home(request):
    return render(request, "pages/home.html", {})
