import json
from django.http import JsonResponse
from app.services.transaction_service import process_transaction


def create_transaction_view(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)

            # futuramente vem do auth
            user_id = 1  

            process_transaction(body, user_id)

            return JsonResponse({"status": "created"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)