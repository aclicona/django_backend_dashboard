import strawberry
import strawberry_django
from strawberry.types import Info
from strawberry import auto
from gqlauth.user.types_ import USER_MODEL, USER_FIELDS, UserFilter, UserStatusType
from gqlauth.core.utils import inject_fields

from versatileimagefield.fields import VersatileImageField
from typing import Any


# Define a custom scalar for handling image URLs
@strawberry.scalar(description="A custom scalar for image URLs")
class ImageURL:
    @staticmethod
    def serialize(url: VersatileImageField) -> str:
        return url.url if url else ""

    @staticmethod
    def parse_value(value: Any) -> VersatileImageField:
        raise NotImplementedError("ImageURL parse_value is not implemented")


@strawberry_django.type(model=USER_MODEL, filters=UserFilter)
@inject_fields(USER_FIELDS, annotations_only=True)
class MyUserType:
    logentry_set: auto
    is_superuser: auto
    last_login: auto
    is_staff: auto
    is_active: auto
    date_joined: auto
    status: UserStatusType
    image: ImageURL  # Add the avatar field here

    @strawberry_django.field
    def archived(self, info: Info) -> bool:
        return self.status.archived

    @strawberry_django.field
    def verified(self, info: Info) -> bool:
        return self.status.verified
