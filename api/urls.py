from django.urls import include, path
from rest_framework import routers

from . import views
from .item_detail import item_detail, item_list
from .approve_request import approve_request
from .views import login


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'requests', views.RequestViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', login),  # Define the login endpoint
    path("item/<int:item_id>/", item_detail, name="item_detail"),
    path("item_list/", item_list, name="item_list"),
    path("request/approve/<int:request_id>/", approve_request, name="approve_request"),
    path("api/item/<int:item_id>/", views.update_item, name="update_item"),  # Add this line
    path("api/request/delete/<int:request_id>/", views.delete_request, name="delete_request"),  # Add this line
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
