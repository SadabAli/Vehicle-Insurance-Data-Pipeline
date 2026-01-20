# from src.logger import logging 

# logging.debug("checking for debug message") 
# logging.info("Checking the Info message") 
# logging.warning("Checking th e warning message") 
# logging.error("Checking the error message") 
# logging.critical("Checking the critical message")


# # below code is to check the exception config
from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1+'Z'
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e

# --------------------------------------------------------------------------------

# from src.pipline.training_pipeline import TrainPipeline

# pipline = TrainPipeline()
# pipline.run_pipeline()