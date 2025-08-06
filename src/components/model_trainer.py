import os
import sys
from src.logger.logger_method import logging
from src.exception.Exception import CustomException
from utils.utils import evaluate_model, save_object
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet


class ModelTrainerConfig:
    model_obj_path = os.path.join("artifact", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_arr, test_arr):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, X_test, y_train, y_test = train_arr.iloc[:, :-1], test_arr.iloc[:, :-1], train_arr[:, -1], test_arr[:, -1]

            # Sunny Code
            # I was not able to come up with this implementation code
            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'Elasticnet': ElasticNet()
            }

            model_report = evaluate_model(X_train, y_train, X_test, y_test, models)

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).items(best_model_score)]

            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            # Till here

            """
            Mine:

            This is the code i wrote to get the best score and get the best model name....which is not complete and correct as well
            final_r2 = max(training_report)

            best_model = training_report.items(final_r2)
            """

            save_object(self.model_trainer_config.model_obj_path, best_model)

        except Exception as e:
            logging.info("Error occurred in Model Training")
            raise CustomException(sys, e)
