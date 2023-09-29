from django.http import HttpResponse
from django.http import JsonResponse, Http404
from .models import Item


def index(request):
    return HttpResponse("Hello CS633")


def item_detail(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
        data = {
            "id": item.id,
            "name": item.name,
            "qty": item.qty,
            "vendor": item.vendor,
        }
        return JsonResponse(data)
    except Item.DoesNotExist:
        raise Http404("Item not found")
