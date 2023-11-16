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
    price = models.IntegerField()
    address = models.TextField()
    lat = models.TextField()
    lon = models.TextField()
    desc = models.TextField() #점주 멘트

class Review(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()
    image_url = models.TextField(null=True, blank=True)

class Tag(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.TextField()