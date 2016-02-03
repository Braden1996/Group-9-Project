"""camel2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from camelcore.views import index as camelcore_index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    # go to core to obtain index
    url(r'^$', camelcore_index, name='index'),

    # user app
    url(r'^user/', include('user.urls', namespace="user")),

    # module app
    url(r'^module/', include('module.urls', namespace="module")),

    url(r"^latexbook/", include("latexbook.urls", namespace="latexbook")),
]
