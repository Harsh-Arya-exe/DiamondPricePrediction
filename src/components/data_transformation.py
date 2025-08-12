import os
import sys
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.logger.logger_method import logging
from sklearn.compose import ColumnTransformer
from src.exception.Exception import CustomException
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from src.utils.utils import save_object


class DataTransformationConfig:
    # preprocessor_obj_path = os.path.join("artifact", "preprocessor.pkl") Mine
    preprocess_obj_file_path = os.path.join("artifact", "preprocessor.pkl")  # Sunny code


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation(self):
        try:
            logging.info("Data Transformation Initiated")

            # Sunny code
            categorical_cols = ['cut', 'color', 'clarity']
            numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']

            # Below is my code where i took the train and test data and tried to find the num and cat cols from them but here, the nums and cols are to be
            # mentioned and also
            # their order(if exists) for the encoding

            """ Mine
            def get_data_transformation(self, train_data, test_data)  No train and test data taken as input in this function 

            train_df = pd.read_csv(train_data)
            test_df = pd.read_csv(test_data)

            num_cols = train_df.select_dtypes(include="np.number")
            cat_cols = test_df.select_dtypes(exclude="np.number")
          """

            cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

            # Mine
            numerical_pipeline = Pipeline(
               steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            # Mine
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    # ("encoder", OrdinalEncoder()), Mine
                    ('ordinalencoder', OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories])),  # Sunny Code
                    ("scaler", StandardScaler())
                ]
            )

            # Mine
            preprocessor = ColumnTransformer(
                transformers=[
                    ("numerical_pipeline", numerical_pipeline, numerical_cols),
                    ("categorical_pipeline", categorical_pipeline, categorical_cols)
                ]
            )

            """
            Mine:
            I thought that the model should be saved and then return it
            save_model(self.data_transformation_config.preprocessor_obj_path, preprocessor)
            """

            return preprocessor

        except Exception as e:
            logging.info("Error occurred in get data transformation function in Data Transformation")
            raise CustomException(sys, e)

    def initiate_data_transformation(self, train_path, test_path):
        try:

            train_df = pd.read_csv(train_path)  # I didn't write these
            test_df = pd.read_csv(test_path)    # two lines in this function

            logging.info("read train and test data complete")
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head : \n{test_df.head().to_string()}')

            preprocess_obj = self.get_data_transformation()  # Mine: This is correct, i wrote this line where we are getting the model

            target_column_name = 'price'  # I wrote the lines after the train test split
            drop_columns = [target_column_name, 'id']

            # I wrote the code for dropping the columns but that was not very clean or correct
            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]

            """ This was the code that i write

            But my thought was correct i.e. to drop the columns

            train_data_df = X_train.drop(labels=[f"{self.columns_to_remove}", f"{self.target_column}"])
            test_data_df = X_test.drop(labels=[f"{self.columns_to_remove}", f"{self.target_column}"])
            """
            # Similarly writing for the testing set
            input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df[target_column_name]

            # I did the preprocessing step

            # Mine but slighty corrected
            input_feature_train_arr = preprocess_obj.fit_transform(input_feature_train_df)

            input_feature_test_arr = preprocess_obj.transform(input_feature_test_df)

            """ This was the code i wrote but the variable names were different

            X_train, X_test, y_train, y_test = train_data.iloc[:, :-1], test_data.iloc[:, :-1], train_data.iloc[:, -1], test_data.iloc[:, -1]

            ===========================================================
            This X_train and X_test came from here
            ===========================================================

            input_feature_train_arr = preprocessor_model.fit_tranform(X_train)

            input_feature_test_arr = preprocessor_model.transform(X_test)
            """

            # self.columns_to_remove = 'id' Mine
            # self.target_column = 'price' Mine

            # self.feature_columns = X_train.drop(labels=[f"{self.columns_to_remove}", f"{self.target_column}"])

            # Sunny Code
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocess_obj_file_path,
                obj=preprocess_obj
            )

            return (
                train_arr,
                test_arr
            )
        except Exception as e:
            logging.info("Error occurred in Data Transformation")
            raise CustomException(sys, e)
