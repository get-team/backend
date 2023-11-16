from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json
from .models import Store

def index(request):
    return HttpResponse("Success!!")

def get_store_list(request):
    stores = Store.objects.all()
    # store_list = serializers.serialize("json", stores)

    json_result = {
        "code": "success"
    }


    return JsonResponse(json_result)


# API
# Create user
# Read review list
# Create review