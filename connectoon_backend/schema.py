import graphene
import connectoon.schema

class Query(connectoon.schema.Query, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)