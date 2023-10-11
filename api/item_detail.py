from django.http import JsonResponse, Http404
from .models import Item


def item_list(request):
    items = Item.objects.all()
    data = [
        {
            "id": item.id,
            "name": item.name,
            "qty": item.qty,
            "vendor": item.vendor,
            "catalog": item.catalog,
            "lastOrderDate": item.lastOrderDate,
            "lastReceivedDate": item.lastReceivedDate,
        }
        for item in items
    ]
    return JsonResponse(data, safe=False)


def item_detail(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
        data = {
            "id": item.id,
            "name": item.name,
            "qty": item.qty,
            "vendor": item.vendor,
            "catalog": item.catalog,
            "lastOrderDate": item.lastOrderDate,
            "lastReceivedDate": item.lastReceivedDate,
        }
        return JsonResponse(data)
    except Item.DoesNotExist:
        raise Http404("Item not found")
