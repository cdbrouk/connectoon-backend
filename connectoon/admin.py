from django.contrib import admin
from .models import Author, WebToon, Toon

# Register your models here.
admin.site.register(Author)
admin.site.register(WebToon)
admin.site.register(Toon)