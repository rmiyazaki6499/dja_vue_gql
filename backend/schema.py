import graphene
import apps.company.schema


class Query(apps.company.schema.Query, graphene.ObjectType):
    pass


class Mutation(apps.company.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
