from django.conf.urls import url

from . import views

app_name='recipes'


urlpatterns = [
    url(r"^$", views.recipe_base, name="recipe_base"),
    url(r'^rotd/$', views.rotd, name='rotd')

    ]
