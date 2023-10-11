from django.urls import path

from . import views
from .item_detail import item_detail, item_list


urlpatterns = [
    path("", views.index, name="index"),
    path("item/<int:item_id>/", item_detail, name="item_detail"),
    path("item_list/", item_list, name="item_list"),
]