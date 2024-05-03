import time
from logging import Logger
from functools import wraps
from typing import (Callable, Any)


class TimeDecorator:
    def __init__(self, logger : Logger = None) -> None:
        """
        Time Decorator.
        """
        self._logger = logger if logger else False

    @property
    def logger(self) -> None:
        return self._logger

    @logger.setter
    def logger(self, value : Logger) -> None:
        self._logger = value

    @logger.deleter
    def logger(self) -> None:
        del_msg = "The property of `TimeDecorator.logger` is not actually deleting. Which it means you cannot save memory by doing this."
        if isinstance(self._logger, Logger):
            self._logger.info(del_msg)
        else:
            print(del_msg)
        self._logger = None

    def __call__(self, func : Callable) -> Callable:
        """
        time decorator.
        """
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            _start_time = time.time()
            _result = func(*args, **kwargs)
            _end_time = time.time()
            _msg = f"<{func.__name__}> Processing Time: {end_time - start_time:.4f} sec."
            if self._logger:
                self._logger.info(_msg)
            elif not self._logger:
                print(_msg)
            else:
                raise Exception(f"You can see this exception message, when the type of `TimeDecorator.logger` is neither `logging.Logger` nor `None`.")
            return _result
        return wrapper