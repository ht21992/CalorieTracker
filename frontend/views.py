from django.shortcuts import render
import json
import requests
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
import pickle
import pandas as pd
from .utils import convert_status_to_description


MODEL_PICKLE_FILE = "BMI_model.pkl"

@require_http_methods(["GET"])
def index(request):
    return render(request, "index.html", context={"view_name":"calorie_tracker"})

@require_http_methods(["GET"])
def get_partial_view(request):
    view_name = request.GET.get("view_name","calorie_tracker")


    return render(request, f"{view_name}.html")

@require_http_methods(["POST"])
def predict_status(request):

    height = request.POST.get("height","")
    weight = request.POST.get("weight","")
    gender = request.POST.get("gender",0)

    with open(MODEL_PICKLE_FILE, 'rb') as file:
        loaded_model=pickle.load(open(MODEL_PICKLE_FILE, 'rb'))

    person = {'Gender': [gender], 'Height': [height], 'Weight': [weight]}

    person_df = pd.DataFrame(person)
    prediction = loaded_model.predict(person_df)
    status_label = convert_status_to_description(prediction)
    return HttpResponse(status_label)

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
        if len(resp) > 1:
            total = {'name': 'total'}
            for key in resp[0].keys():
                if key == 'name':
                    continue
                total[key] = round(sum(item[key] for item in resp),2)
            resp.append(total)

    except Exception as e:
        print(e)
        return HttpResponse(f"oops! There was an error")
    return render(request, "partials/food_info.html", {'resp': resp})
