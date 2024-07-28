"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from .apps.graph.views import GraphQLPlaygroundView
from .apps.graph.schema import schema
from strawberry.django.views import AsyncGraphQLView
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', AsyncGraphQLView.as_view(schema=schema)),
    path("playground", csrf_exempt(GraphQLPlaygroundView.as_view(endpoint="/graphql"))),
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
    re_path(r'^dmedia/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),

    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': os.path.join(settings.VUE_ROOT, 'media')}),
    re_path(r'^src/assets/img/(?P<path>.*)$', serve,
            {'document_root': os.path.join(settings.VUE_ROOT, 'src', 'assets', 'img')}),
    re_path(r'^src/assets/js/(?P<path>.*)$', serve,
            {'document_root': os.path.join(settings.VUE_ROOT, 'src', 'assets', 'js')}),
    re_path(r'^src/assets/css/(?P<path>.*)$', serve,
            {'document_root': os.path.join(settings.VUE_ROOT, 'src', 'assets', 'css')}),
    re_path(r'^src/assets/fonts/(?P<path>.*)$', serve,
            {'document_root': os.path.join(settings.VUE_ROOT, 'src', 'assets', 'fonts')}),
    re_path(r'^(?P<path>.*)$', TemplateView.as_view(template_name="index.html")),
]
