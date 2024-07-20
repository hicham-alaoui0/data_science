import sys
import traceback

# Exception hook to print stack trace
def exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)
    sys.__excepthook__(exctype, value, tb)
sys.excepthook = exception_hook

# Main function to raise an exception
def main():
    raise Exception('This is an exception')