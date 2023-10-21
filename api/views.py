from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .models import Item


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
