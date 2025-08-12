from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

# Starting the data ingestion
ingestion_obj = DataIngestion()
train_path, test_path = ingestion_obj.initiate_data_ingestion()

# Starting the data DataTransformation
transformation_obj = DataTransformation()
train_arr, test_arr = transformation_obj.initiate_data_transformation(train_path, test_path)

# Starting the model training
model_trainer_obj = ModelTrainer()
model_trainer_obj.initiate_model_training(train_arr, test_arr)

model_evaluation_obj = ModelEvaluation()
model_evaluation_obj.initiate_model_evaluation(test_arr)
