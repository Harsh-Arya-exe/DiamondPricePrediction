import sys


class CustomException(Exception):

    def __init__(self, error_details: sys, error_message):
        self.error_message = error_message  # error message
        _, _, error_traceback_obj = error_details.exc_info()  # this returns a tuple (exc_type, exc_value, exc_traceback) so we only took exc_traceback obj
        self.filename = error_traceback_obj.tb_frame.f_code.co_filename  # what i think it is error_traceback_obj.traceback_fram.file_code.code_filename
        self.lineno = error_traceback_obj.tb_lineno

    def __str__(self):
        return f"Error [{self.error_message}] occurred at line number [{self.lineno}] in file [{self.filename}]"


if __name__ == '__main__':
    try:
        x = 1/0
    except Exception as e:
        print(CustomException(sys, e))
