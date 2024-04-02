from django.shortcuts import render
import json
import requests
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings


@require_http_methods(["GET"])
def index(request):
    return render(request, "index.html")


@require_http_methods(["POST"])
def get_food_info(request):
    food_query = request.POST.get("query", "")
    if not food_query:
        return HttpResponse("Food field is empty")
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
    api_request = requests.get(
        api_url + food_query, headers={'X-Api-Key': settings.FOOD_API_KEY})
    try:
        if not api_request.json():
            return HttpResponse(f"Nothing found for {food_query}")
        resp = json.loads(api_request.content)
    except Exception as e:
        print(e)
        return HttpResponse(f"oops! There was an error")
    return render(request, "partials/food_info.html", {'resp': resp})
