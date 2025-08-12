import os
import sys
import pickle
from src.exception.Exception import CustomException
from sklearn.metrics import r2_score


# Sunny Code
def save_object(file_path, obj):
    try:  # In my code i missed the try except block and also forgot to add logic to make the directory if it does not exists
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(sys, e)


def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]

            model.fit(X_train, y_train)

            pred = model.predict(X_test)

            r2 = r2_score(y_test, pred)

            report[list(models.keys())[i]] = r2

            return report
    except Exception as e:
        raise CustomException(sys, e)


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(sys, e)


"""
This was the logic that i wrote
def save_object(file_path, model_name):
    with open(file_path, 'wb'):
        pickle.dump(model_name)


def load_object(obj_name):
    with open("artifact", 'rb'):
        pickle.load(obj_name)


def evaluate_model(y_true, predictions, models):
    r2 = r2_score(y_true, predictions)

    mae = mean_absolute_error(y_true, predictions)

    mse = mean_squared_error(y_true, predictions)

    return r2, mae, mse
"""
