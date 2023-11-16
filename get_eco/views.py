from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json
from .models import Store

def get_store_list(request):
    stores = Store.objects.all()
    # store_list = serializers.serialize("json", stores)

    json_result = {
        "code": "success"
    }

    store_list = []
    for store in stores:
        store_list.append(store.id)

    json_result["store_list"] = store_list

    return JsonResponse(json_result)


# API
# Create user
# Read review list
# Create review