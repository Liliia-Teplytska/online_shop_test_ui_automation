import logging
import datetime
import os

# Add loggers to .log file and file with test results
class Logger:
    log_file = f"logs/log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

    @staticmethod
    def setup_logger():
        logging.basicConfig(filename=Logger.log_file, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    def write_log_to_file(data: str):
        Logger.setup_logger()
        logger = logging.getLogger()

    @staticmethod
    def checking(method_name: str, browser_name: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Browser: {browser_name}\n"  # Browser info
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Test: {method_name}\n"      # name of testing method
        print(data_to_add)

        Logger.write_log_to_file(data_to_add)