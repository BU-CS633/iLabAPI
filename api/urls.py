from django.urls import path

from . import views
from .item_detail import item_detail, item_list
from .approve_request import approve_request

urlpatterns = [
    path("", views.index, name="index"),
    path("item/<int:item_id>/", item_detail, name="item_detail"),
    path("item_list/", item_list, name="item_list"),
    path("request/approve/<int:request_id>/", approve_request, name="approve_request"),
    path("api/item/<int:item_id>/", views.update_item, name="update_item"),  # Add this line
    path("api/request/delete/<int:request_id>/", views.delete_request, name="delete_request"),  # Add this line

