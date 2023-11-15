from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Success!!")

# API
# Read store list
# Create user
# Read review list
# Create review