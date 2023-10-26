from django.urls import path

from . import views
from . import item_detail

urlpatterns = [
    path("", views.index, name="index"),
    path("item/<int:item_id>/", item_detail.item_detail, name="item_detail"),
    path("api/item/<int:item_id>/", views.update_item, name="update_item"),  # Add this line
    path("api/request/delete/<int:request_id>/", views.delete_request, name="delete_request"),  # Add this line

]