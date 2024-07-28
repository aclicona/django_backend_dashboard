from decouple import config
DEV = config('DEV', default=False, cast=bool)
if DEV:
    from .dev import *
else:
    from .prod import *