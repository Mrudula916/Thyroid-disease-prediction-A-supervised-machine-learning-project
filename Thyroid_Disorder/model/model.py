from flask import Blueprint

import joblib
import numpy as np
model = Blueprint('model', __name__)

def predict(dict):
    randomForest = joblib.load("model/thyroid(1).sav")
    inputs = np.array([
        dict["onthyroxine"],
        dict["antithyroidmed"],
        dict["pregnant"],
        dict["hypothyroid"],
        dict["goitre"],
        dict["psych"],
        dict["tsh"],
        dict["t3"],
        dict["tt4"],
        dict["fti"]]).reshape(1,10)

    type = ""
    res = randomForest.predict(inputs)
    if(res):
        type = classify(dict)
    return res[0], type

def classify(dict):
    type =""
    # Checking for Hyperthyroidism
    
    if dict["tsh"] < 0.1 and dict["t3"] > 2.8:
        type = "\nType: Overt Hyperthyroidism"
    elif dict["tsh"] > 4.5:
        type = "\nType: Overt Hypothyroidism"
    elif dict["tsh"] < 0.1 and round(dict["t3"]) in range(0.9, 2.7):
        type = "\nType: Subclinical Hyperthyroidism"
    elif dict["tsh"] >= 10:
        type="\nType: Subclinical Hypothyroidism"
    else:
        type = "\nType: Unkown Type"

    return type
