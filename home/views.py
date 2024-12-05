from django.shortcuts import render


# home/views.py

def home_view(request):
    """
    Renders the About page
    """
    return render(request, 'home/home.html')
