import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

# -----------------------------
# ✅ Constants for log config
# -----------------------------
LOG_DIR = 'logs'
LOG_FILENAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3                # Keep last 3 log files

# -----------------------------
# ✅ Ensure logs directory exists
# -----------------------------
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)

# Full path to the current log file
log_file_path = os.path.join(log_dir_path, LOG_FILENAME)

# -----------------------------
# ✅ Logger Configuration Function
# -----------------------------
def configure_logger():
    """
    Sets up a global logger with:
    - RotatingFileHandler: stores logs in rotating files
    - StreamHandler: prints logs to console
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Capture all logs, even debug

    # Prevent duplicate handlers if configure_logger is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    # Define log format
    formatter = logging.Formatter(
        "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"
    )

    # File handler for persistent log storage
    file_handler = RotatingFileHandler(
        log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)  # Log everything to file

    # Console handler for real-time logs
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)  # Show info+ in console

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# -----------------------------
# ✅ Initialize logging on import
# -----------------------------
configure_logger()
