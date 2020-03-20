from django.db import models

class Author(models.Model):
  name= models.TextField(blank=True)
  title= models.TextField(blank=True)
  career= models.IntegerField(default=0)
  address= models.TextField(blank=True)
  age= models.IntegerField(default=0)
  

class WebToon(models.Model):
  title= models.TextField(blank=True)
  author= models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
  story= models.TextField(blank=True)
  style= models.TextField(blank=True)
  thumbnail_story= models.TextField(blank=True)
  thumbnail_style= models.TextField(blank=True)
  like= models.IntegerField(default=0)
  create_date= models.TextField(blank=True)
  genre = models.TextField(blank=True)

# Create your models here.
class Toon(models.Model):
  webtoon = models.ForeignKey(WebToon, on_delete=models.CASCADE, default=1)
  episode= models.IntegerField(default=0)
  image= models.TextField(blank=True)


