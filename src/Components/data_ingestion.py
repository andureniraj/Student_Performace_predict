import os
import sys
#from exception import CustomException
#from logger import logging
from datetime import datetime
import logging
import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

# Exception code
def error_message_details(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message


class CustomException(Exception):
    def _init_(self,error_message,error_details:sys):
        super()._init_(error_message)
        self.error_message = error_message_details(error_message,error_details)

    def _str_(self):
        return self.error_message
    
#logging code
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
FILE_PATH = os.path.join(os.getcwd(),"logs",LOG_FILE_NAME)
os.makedirs(FILE_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(FILE_PATH,LOG_FILE_NAME)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s- %(levelname)s - %(message)s", 
    level=logging.INFO,)


@dataclass

class DataIngestionConfig:
    train_data = os.path.join('artifacts',"train_data.csv")
    test_data = os.path.join('artifacts',"test_data.csv")
    raw_data = os.path.join('artifacts',"raw_data.csv")

class DataIngestion:
    def __init__(self):
        self.DataIngestionConfig = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            os.makedirs(os.path.dirname(self.DataIngestionConfig.raw_data),exist_ok=True)
            logging.info("Data Ingestion Started")
            file_path = "src\\Components\\Notebook\\Data\\Student_data.csv"
            file_name = os.path.split(file_path)[1]
            file_ext =os.path.splitext(file_name)[1]
            print(file_ext)
            if file_ext == ".csv":
                df = pd.read_csv(file_path)
            if df is not None :
                df.to_csv(self.DataIngestionConfig.raw_data,header=True,index=False)

            logging.info("train-test split started")

            train_data,test_data = train_test_split(df,test_size=0.2,random_state=42)
            train_data.to_csv(self.DataIngestionConfig.train_data,header=True,index=False)
            test_data.to_csv(self.DataIngestionConfig.test_data,header=True,index=False)
            logging.info("data ingestion complted")
            return(
                self.DataIngestionConfig.train_data,
                self.DataIngestionConfig.test_data

            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj =DataIngestion()
    obj.initiate_data_ingestion()





        

        
    