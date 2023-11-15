from django.db import models

class User(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    nickname = models.TextField()
    phone_number = models.TextField()

class Store(models.Model):
    name = models.TextField()
    start_time = models.TextField()
    end_time = models.TextField()
    menu_name = models.TextField()
    price = models.TextField()
    address = models.TextField()
    lat = models.TextField()
    lon = models.TextField()
    desc = models.TextField() #점주 멘트
    tags = models.TextField()