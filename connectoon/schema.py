import graphene
from graphene_django import DjangoObjectType 
from django.db.models import Q
from .models import Toon, WebToon, Author

class AuthorType(DjangoObjectType):
  class Meta:
    model = Author

class WebToonType(DjangoObjectType):
  class Meta:
    model = WebToon

class ToonType(DjangoObjectType):
  class Meta:
    model = Toon

class Query(graphene.ObjectType):
  authors = graphene.List(AuthorType, search=graphene.String())
  webtoons = graphene.List(WebToonType, story=graphene.String(), style=graphene.String())
  toons = graphene.List(ToonType, search=graphene.String()) 

  def resolve_authors(self, info, search=None,**kwargs):
    if search:
      filter = Q(name__icontains=search)
      return Author.objects.filter(filter)
    return Author.objects.all()

  def resolve_webtoons(self, info, story=None, style=None, **kwargs):
    if story:
      if story=='전체보기': return WebToon.objects.exclude(story='')
      filter = Q(story__icontains=story)
      return WebToon.objects.filter(filter)
    if style:
      if style=='전체보기': return WebToon.objects.exclude(style='')
      filter = Q(style__icontains=style)
      return WebToon.objects.filter(filter)
    return WebToon.objects.all();

  def resolve_toons(self, info, search=None,**kwargs):
    if search:
      filter = Q(webtoon__title__icontains=search)
      return Toon.objects.filter(filter)
    return Toon.objects.all()
      