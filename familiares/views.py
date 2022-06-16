from django.shortcuts import render
from .models import Familia

def index(request):
    familias = Familia.objects.all()
    ctx = {'familias': familias}
    return render(request, "familiares/index.html",ctx)
