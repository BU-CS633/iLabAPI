from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Item, Request, Status


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'fullName', 'unitSize', 'qty']


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    item = ItemSerializer()
    owner = UserSerializer()
    status = serializers.SlugRelatedField(
        read_only=True,
        slug_field='description',
    )

    class Meta:
        model = Request
        fields = ['owner', 'item', 'request_date', 'order_date', 'received_date', 'approved_date', 'receivedBy',
                  'status']
