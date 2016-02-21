from django.conf.urls import include, url
from . import views

from module.views import ModuleIndexView

app_name = 'module'
urlpatterns = [
    url(r'^$', ModuleIndexView.as_view(), name='module_index'),
    url(r'^(?P<pk>\w+)/$', views.module_detail, name="module_detail"),
    url(r"^(?P<module_pk>\w+)/", include("latexbook.urls", namespace="latexbook"))
]