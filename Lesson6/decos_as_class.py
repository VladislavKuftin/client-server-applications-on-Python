import inspect
import logging
import sys

sys.path.append('../')
import logs.config_client_log
import logs.config_server_log
from functools import wraps


class MyFilter(logging.Filter):
    def filter(self, record):
        return "фУнкция" in record.getMessage()


class Log:
    def __init__(self, logger=None):
        self.logger = logger

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            parent_func_name = inspect.currentframe().f_back.f_code.co_name
            module_name = inspect.currentframe().f_back.f_code.co_filename.split("/")[-1]
            if self.logger is None:
                logger_name = module_name.replace('.py', '')
                self.logger = logging.getLogger(logger_name)


            new_filter = MyFilter()
            self.logger.addFilter(new_filter)
            print('List of filters after adding new_filter: ', self.logger.filters)


            self.logger.debug(f'фУнкция {func.__name__} вызвана из функции {parent_func_name} '
                              f'в модуле {module_name} с аргументами: {args}; {kwargs}')


            self.logger.debug(f'Функция {func.__name__} вызвана из функции {parent_func_name} '
                              f'в модуле {module_name} с аргументами: {args}; {kwargs}')


            self.logger.filters.remove(new_filter)
            print('List of filters after removing new_filter: ', self.logger.filters)

            result = func(*args, **kwargs)
            return result
        return wrapper
