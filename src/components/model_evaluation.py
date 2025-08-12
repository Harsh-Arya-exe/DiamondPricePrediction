import os
import sys
import numpy as np
from src.logger.logger_method import logging
from src.exception.Exception import CustomException
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from src.utils.utils import load_object
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse


class ModelEvaluation:
    def __init__(self):
        # Sunny: Missed this logging statement
        logging.info("evaluation started")

    def evaluate_metric(self, actual, pred):
        # Mine
        rmse = np.sqrt(mean_squared_error(actual, pred))
        r2 = r2_score(actual, pred)
        mae = mean_absolute_error(actual, pred)
        logging.info("evaluation metrics captured")
        return r2, rmse, mae

    def initiate_model_evaluation(self, test_arr):
        try:

            X_test, y_test = test_arr[:, :-1], test_arr[:, -1]

            model = load_object(os.path.join("artifact", "model.pkl"))

            # mlflow.set_tracking_uri()

            """
            Mine: This i Wrote but to be written inside mlflow.start_run()
            pred = model.predict(X_test)

            r2, rmse, mae = self.evaluate_metric(y_test, pred)

            Mine : I wrote this line , the correct line is written below

            tracking_uri_type = urlparse(mlflow.get_tracking_uri())
            """

            tracking_url_type_store = urlparse(mlflow.get_artifact_uri()).scheme

            print(tracking_url_type_store)

            mlflow.set_experiment("Mlflow-01")

            if mlflow.active_run():
                mlflow.end_run()

            with mlflow.start_run():

                # These lines are to be written here
                predictions = model.predict(X_test)

                # This line too
                (r2, rmse, mae) = self.evaluate_metric(y_test, predictions)

                mlflow.log_metric("r2", r2)
                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("mae", mae)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
            else:
                mlflow.sklearn.log_model(model, "model")
        except Exception as e:
            raise CustomException(sys, e)
