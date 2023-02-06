import pandas as pd
import numpy as np
import json
import pickle

DATABASE = pd.read_csv('assets/Restaurant_Metadata_CLEANED.csv')
f = open('assets/sentiments.json')
SENTIMENTS = json.load(f)
f.close()

class RestaurantMetadata:
    def __init__(self, name, cuisine, img_link, cost, rating, n_ratings, address):
        self.name = name
        self.cuisine = cuisine
        self.img_link = img_link
        self.cost = cost
        self.rating = float(rating)
        self.n_ratings = int(n_ratings.replace(',', ''))
        self.address = address
        self.sentiments = [sentiment for sentiment in SENTIMENTS[name].keys() if SENTIMENTS[name][sentiment] > 75]

def get_restaurants_by_name(names):
    restaurants = DATABASE[DATABASE['name'].isin(names)].to_dict('records')
    return [RestaurantMetadata(**restaurant) for restaurant in restaurants]
