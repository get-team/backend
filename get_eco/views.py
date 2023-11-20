from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json
from .models import Store

def get_store_list(request):
    stores = Store.objects.all()
    # store_list = serializers.serialize("json", stores)

    store_list = []
    for store in stores:
        store_json = {
            "id": store.id,
            "name": store.name,
            "menu": store.menu_name,
            "address": store.address
        }
        store_list.append(store_json)

    json_result = {
        "code": "success",
        "data": {
            "store_list": store_list,
            "store_count": len(store_list),
            "type": "all"
        }
    }

    return JsonResponse(json_result)


# API
# Create user
# Read review list
# Create review