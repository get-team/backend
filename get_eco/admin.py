from django.contrib import admin
from .models import User
from .models import Store
from .models import Review
from .models import Tag

admin.site.register(User)
admin.site.register(Store)
admin.site.register(Review)
admin.site.register(Tag)
