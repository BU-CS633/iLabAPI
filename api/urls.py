from django.urls import path

from . import views
from . import item_detail

urlpatterns = [
    path("", views.index, name="index"),
    path("item/<int:item_id>/", item_detail.item_detail, name="item_detail"),
]