from django.shortcuts import render
import requests
import numpy as np

# Create your views here.
def recipe_base(request):
    return render(request, 'recipes/recipe_base.html', context={})



def get_recipe():


    random_num = np.random.randint(1,999999)

    url = f'https://api.spoonacular.com/recipes/{random_num}/information?apiKey=d955d2635248430f9f297dbbbc8229d3'

    try:
        req = requests.get(url)

        req_json = req.json()

        print('Your random recipe is for ' + req_json['title'] + '!')

        return req_json

    except:
        return 'API Request failed!'



def rotd(request):
    recipe_today = get_recipe()
    return render(request, 'recipes/rotd.html', context=recipe_today)
