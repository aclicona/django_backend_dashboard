from django import template
from django.db.models import Sum
from django.conf import settings

register = template.Library()


def get_host():
    return 'test-wap121.test.epm.com.co:8888/'


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.
    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.
    For example, if you're on the page ``/things/?with_frosting=true&page=5``,
    then
    <a href="/things/?{% param_replace page=3 %}">Page 3</a>
    would expand to
    <a href="/things/?with_frosting=true&page=3">Page 3</a>
    Based on
    https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


@register.simple_tag
def site_name(**kwargs):
    return settings.SITE_NAME


@register.simple_tag
def protocol(**kwargs):
    try:
        return 'http' if settings.DEBUG or settings.LOCAL_PROD else 'https'
    except AttributeError:
        return 'https'


@register.simple_tag
def domain(**kwargs):
    return get_host()


@register.simple_tag
def frontend_protocol(**kwargs):
    return settings.FRONTEND_SCHEME


@register.simple_tag
def frontend_domain(**kwargs):
    return settings.FRONTEND_HOST
