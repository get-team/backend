from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json
from .models import Store, Review

def get_store_list(request):
    stores = Store.objects.all()
    # store_list = serializers.serialize("json", stores)

    store_list = []
    for store in stores:
        store_json = {
            "id": store.id,
            "startTime": store.start_time,
            "endTime": store.end_time,
            "menu": store.menu_name,
            "price": store.price,
            "address": store.address,
            "lat": store.lat,
            "lon": store.lon,
            "promotion": store.desc
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

def get_review_list(request):
    reviews = Review.objects.all()

    review_list = []
    for review in reviews:
        review_json = {
            "id": review.id,
            "createTime": review.created_time,
            "user": review.user,
            "store": review.store,
            "rating": review.rating,
            "imageURL": review.image_url
        }

    json_result2 = {
        "code": "success",
        "data": {
            "review_list": review_list,
            "review_count": len(review_list),
            "type": "all"
        }
    }
    return JsonResponse(json_result2)

# API
# Create user
# Read review list
# Create review