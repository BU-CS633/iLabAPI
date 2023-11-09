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
    item = serializers.SlugRelatedField(
        queryset=Item.objects.all(),
        slug_field='name',
    )
    owner = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )
    status = serializers.SlugRelatedField(
        read_only=True,
        slug_field='description',
    )

    class Meta:
        model = Request
        fields = ['item', 'owner', 'request_date', 'status']


