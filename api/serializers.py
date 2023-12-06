from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Item, Request


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
        fields = ['name', 'fullName', 'unitSize', 'qty', 'price', 'vendor', 'catalog', 'lastOrderDate',
                  'lastReceivedDate', 'channel', 'location', 'link', 'notes', 'id']


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user_is_admin = serializers.SerializerMethodField()

    def get_user_is_admin(self, obj):
        # Retrieve the 'user_is_admin' context and return it
        return self.context.get('user_is_admin', False)

    status = serializers.SlugRelatedField(
        read_only=True,
        slug_field='description',
    )
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = ['owner', 'item', 'request_date', 'order_date', 'received_date',
                  'approved_date', 'receivedBy', 'status', 'quantity_requested',
                  'total_price', 'request_notes', 'id', 'user_is_admin']

    @staticmethod
    def get_total_price(obj):
        total_price = obj.total_price()
        return round(total_price, 3)

    def to_representation(self, instance):
        """
        Modify the representation of the serializer to include username and item name.
        """
        representation = super().to_representation(instance)

        # Add the username of the owner
        representation['owner_username'] = instance.owner.username if instance.owner else None

        # Add the name of the item
        representation['item_name'] = instance.item.name if instance.item else None

        return representation

