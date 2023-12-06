from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .models import Item
from .models import Request

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ItemSerializer, RequestSerializer

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.authentication import TokenAuthentication

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

    else:
        return Response({'error': 'Invalid Credentials'}, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_details(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        # Add other user details you want to expose
    })


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Assuming the user model uses 'id' as the primary key
        user_id = request.user.id
        return Response({'user_id': user_id})


class ItemViewSet(viewsets.ModelViewSet):
    ...
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    return HttpResponse("Hello CS633")


@require_POST
def update_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)  # Fetch the item

        # Extract data from POST request and update item attributes
        item.name = request.POST.get('name', item.name)
        item.qty = int(request.POST.get('qty', item.qty))
        item.vendor = request.POST.get('vendor', item.vendor)
        item.catalog = request.POST.get('catalog', item.catalog)

        # Handle date fields; if date is provided in POST data, parse it, otherwise use existing value
        if 'lastOrderDate' in request.POST:
            item.lastOrderDate = datetime.strptime(request.POST['lastOrderDate'], '%Y-%m-%d').date()
        if 'lastReceivedDate' in request.POST:
            item.lastReceivedDate = datetime.strptime(request.POST['lastReceivedDate'], '%Y-%m-%d').date()

        item.save()  # Save the updated item

        return JsonResponse({'status': 'success', 'message': 'Item updated successfully'})
    except Item.DoesNotExist:
        return HttpResponse(status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


def delete_request(request, request_id):
    try:
        request_obj = Request.objects.get(pk=request_id)
        request_obj.delete()
        return JsonResponse({'status': 'success', 'message': 'Request deleted successfully'})
    except Request.DoesNotExist:
        return HttpResponse(status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all().order_by('id')  # Order the queryset
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Request.objects.all().order_by('id')
    serializer_class = RequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['item__id']

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        context = super().get_serializer_context()
        # Add any custom context here
        return context
