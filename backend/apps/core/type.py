import graphene


class SelectType(graphene.ObjectType):
    name = graphene.String()
    value = graphene.Int()

    def resolve_name(self, info, **kwargs):
        return self.get('name', None)

    def resolve_value(self, info, **kwargs):
        return self.get('value', None)


class SelectTypeStr(graphene.ObjectType):
    name = graphene.String()
    value = graphene.String()

    def resolve_name(self, info, **kwargs):
        return self.get('name', None)

    def resolve_value(self, info, **kwargs):
        return self.get('value', None)
