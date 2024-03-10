import sys
from logger import logging


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

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Cant divide by 0")
        raise CustomException(e,sys)
    