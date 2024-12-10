# views.py
from django.shortcuts import render

def main(request):
    return render(request, 'rooms.html')  # Ensure you have a 'home.html' template
