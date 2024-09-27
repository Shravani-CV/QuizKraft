import os
import logging
import datetime


# strftime gives the current datetime in below format 
# so we name the log the same so we can keep track of it.
LOG_FILE = f"{datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# os.getcwd gets us current working dir, join function is used to join it with logs and 
# then new file name is created.
log_path = os.path.join(os.getcwd(),"logs")
# makes directory with given path
os.makedirs(log_path,exist_ok=True)
# Creates a file with given name at given path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    level = logging.INFO,
    filename = LOG_FILEPATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)