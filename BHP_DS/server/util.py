import pandas as pd
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    if len(__data_columns) == 0:
        print("Error: __data_columns is empty. Please make sure that the data.csv file is correct.")
        return None

    if loc_index == -1:
        print(f"Error: Location '{location}' not found in the data. Please check the spelling and try again.")
        return None

    X = [0] * len(__data_columns)
    X[0] = sqft
    X[2] = 5 - bath
    X[1] = bhk
    if loc_index >= 0:
        X[loc_index] = 1
    print(X)
    return round(__model.predict([X])[0], 2)

def get_location_names():
    print(__locations)
    print('444555')
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    __data_columns = []  # Initialize as empty list
    __locations = []     # Initialize as empty list

    with open("E:/DS LAB/BHP_DS/server/artifacts/data.csv", "r") as f:
        next(f)  # Skip the first line if it is not a valid header row
        for line in f:
            __data_columns.append(line.strip().split(",")[0])

    __locations = __data_columns[3:]

    global __model
    if __model is None:
        with open("E:/DS LAB/BHP_DS/server/artifacts/banglore_home_prices_model.pickle", "rb") as file:
            __model = pickle.load(file)

    print("loading saved artifacts...done")
    print(__data_columns)


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 2))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))