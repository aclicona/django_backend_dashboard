from gqlauth.core.middlewares import JwtSchema
from ..account.schema.query import UserQueries
from ..account.schema.mutation import UserMutations


class Query(UserQueries
            ):
    """root query"""


class Mutation(UserMutations
               ):
    """root query"""


schema = JwtSchema(query=Query, mutation=Mutation)
