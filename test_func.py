# resp =[{'name': 'beer', 'calories': 43.3, 'serving_size_g': 100.0, 'fat_total_g': 0.0, 'fat_saturated_g': 0.0, 'protein_g': 0.5, 'sodium_mg': 3, 'potassium_mg': 13, 'cholesterol_mg': 0, 'carbohydrates_total_g': 3.6, 'fiber_g': 0.0, 'sugar_g': 0.0}, {'name': 'salt', 'calories': 0.0, 'serving_size_g': 100.0, 'fat_total_g': 0.0, 'fat_saturated_g': 0.0, 'protein_g': 0.0, 'sodium_mg': 38395, 'potassium_mg': 0, 'cholesterol_mg': 0, 'carbohydrates_total_g': 0.0, 'fiber_g': 0.0, 'sugar_g': 0.0}]

# total = {'name': 'total'}
# for key in resp[0].keys():
#     if key == 'name':
#         continue
#     total[key] = sum(item[key] for item in resp)



# # total = {'name': 'total', **{key: sum(item[key] for item in resp) for key in resp[0].keys() if key != 'name'}}


# print(total)



import requests

muscle = 'abdominals'
exc_type="strength"
difficulty="expert"
api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}&type={}&difficulty={}'.format(muscle,exc_type,difficulty)
response = requests.get(api_url, headers={'X-Api-Key': 'XwyEO4+qY3Mv0dI8Lcy0bQ==ibpwNTE4xUUU6XOu'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)