import logging
import os
from datetime import datetime

# Log file name for different files
LOG_FILE = f"{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log"

# making directory

log_path = os.path.join(os.getcwd(), "logs")  # folder name

os.makedirs(log_path, exist_ok=True)  # making the dir

file_path = os.path.join(log_path, LOG_FILE)  # file name

# LOGGING INFO

logging.basicConfig(
    level=logging.INFO,
    filename=file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s %(message)s"
)
