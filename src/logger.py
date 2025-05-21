import logging
import os
from datetime import datetime

LOG_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_file)
os.makedirs(log_path,exist_ok=True)


LOG_FILE_PATH=os.path.join(log_path,LOG_file)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,
)

'''below code is to check the logger is working or not , we can see "my_package.egg-info " folder is created
'in terminal write python src/pipeline/logger.py' it will excute the code
'''
if __name__=="__main__":
    logging.info("Logger has started")