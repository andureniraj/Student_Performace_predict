import logging
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
FILE_PATH = os.path.join(os.getcwd(),"logs",LOG_FILE_NAME)
os.makedirs(FILE_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(FILE_PATH,LOG_FILE_NAME)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s- %(levelname)s - %(message)s", 
    level=logging.INFO,)



