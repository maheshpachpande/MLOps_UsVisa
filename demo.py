from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

logging.info("Logging has started")

try:
    a = 1 / 0  # Sample error
except Exception as e:
    raise USvisaException(e, sys)
