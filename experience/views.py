from django.shortcuts import render

# Create your views here.
def experience_page(request):
    return render(request, 'experience/timeline.html')
