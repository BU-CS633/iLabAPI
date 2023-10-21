from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .models import Item


def index(request):
    return HttpResponse("Hello CS633")



