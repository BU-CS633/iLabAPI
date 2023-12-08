from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Request, Status,Item
from django.utils import timezone


@csrf_exempt
def approve_request(request, request_id):
    if request.method == "GET":
        try:
            inventory_request = Request.objects.get(pk=request_id)
            approve_status = Status.objects.get(description="approved")

            inventory_request.status = approve_status
            inventory_request.approved_date = timezone.now()
            inventory_request.save()

            item = Item.objects.get(pk=inventory_request.item_id)
            item.qty = item.qty + inventory_request.quantity_requested
            item.save()

            return JsonResponse({"message": "Request approved successfully!"})
        except Request.DoesNotExist:
            raise Http404("Request not found")
        except Status.DoesNotExist:
            raise Http404("Approve status not found")

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)




