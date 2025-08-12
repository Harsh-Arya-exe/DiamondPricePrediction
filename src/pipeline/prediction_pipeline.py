import os
import sys
import pandas as pd
from src.logger.logger_method import logging
from src.exception.Exception import CustomException
from src.utils.utils import load_object


class CustomData:
    def __init__(self, carat, cut, color, clarity, depth, table, x, y, z):
        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z

    def get_data_as_dataframe(self):
        try:
            # the values are in the list because pandas asks for scalers to be in list because it , understand it as columns
            custom_data_input_dict = {
                    'cut': [self.cut],
                    'color': [self.color],
                    'clarity': [self.clarity],
                    'depth': [self.depth],
                    'table': [self.table],
                    'x': [self.x],
                    'y': [self.y],
                    'z': [self.z],
                    'carat': [self.carat]
                }
            data = pd.DataFrame(custom_data_input_dict)

            return data
        except Exception as e:
            logging.info("Exception Occured in prediction pipeline")
            raise CustomException(sys, e)


class PredictionPipeline:

    def __init__(self):
        print("...init the object")

    def predict(self, features):
        try:

            # Mine
            preprocessor_path = os.path.join("artifact", "preprocessor.pkl")  # preprocessor path for loading
            model_path = os.path.join("artifact", "model.pkl")  # model path to load model

            preprocessor = load_object(preprocessor_path)  # preprocessor obj
            model = load_object(model_path)  # model obj

            scaled_features = preprocessor.transform(features)  # transforming the data

            pred = model.predict(scaled_features)  # prediction

            return pred
        except Exception as e:
            raise CustomException(sys, e)
