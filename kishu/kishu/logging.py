import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("KishuKernel")
file_path = "/Users/matsumotoryutaro/programs/KishuKernel/Kishu.log"
file_handler = RotatingFileHandler(file_path, maxBytes=1024*1024, backupCount=5)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
