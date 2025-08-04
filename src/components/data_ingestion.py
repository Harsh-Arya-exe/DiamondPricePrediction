import pandas as pd
import sys
import os
from sklearn.model_selection import train_test_split
from src.logger.logger_method import logging
from src.exception.Exception import CustomException
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    raw_path = os.path.join("artifact", "raw_data.csv")
    train_path = os.path.join("artifact", "train.csv")
    test_path = os.path.join("artifact", "test.csv")


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:

            logging.info("Starting the data ingestion")

            logging.info("Reading the data")

            """
            data = pd.read_csv(self.raw_path)

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_path), exist_ok=True)

            data.to_csv(self.data_ingestion_config.raw_path, index=False)

            logging.info("Splitting the data into train test split")

            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

            """
            self.train_data_link = "https://raw.githubusercontent.com/Harsh-Arya-exe/Gemstone-data/refs/heads/main/train.csv"
            self.test_data_link = "https://raw.githubusercontent.com/Harsh-Arya-exe/Gemstone-data/refs/heads/main/train.csv"

            logging.info("Saving the files")

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_path), exist_ok=True)

            train_data = pd.read_csv(self.train_data_link)

            test_data = pd.read_csv(self.test_data_link)

            train_data.to_csv(self.data_ingestion_config.train_path, index=False)

            test_data.to_csv(self.data_ingestion_config.test_path, index=False)

            logging.info("Data Ingestion Completed")

            return (
                self.data_ingestion_config.train_path,
                self.data_ingestion_config.test_path
            )

        except Exception as e:
            logging.info("Error occurred in Data Ingestion")
            raise CustomException(sys, e)


if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()
