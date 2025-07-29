import os
import sys
import traceback

def error_message_detail(error: Exception, error_detail) -> str:
    """
    Extracts detailed error message including script name and line number.

    Args:
        error (Exception): The caught exception object.
        error_detail (sys): sys module to extract traceback info.

    Returns:
        str: A formatted error message with file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
    line_number = exc_tb.tb_lineno if exc_tb else "Unknown"
    
    return f"Error in script [{file_name}] at line [{line_number}]: {str(error)}"

class USvisaException(Exception):
    """
    Custom exception class for the US Visa Classifier project.
    Enhances standard exceptions with traceback details.
    """
    def __init__(self, error_message: Exception, error_detail):
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
