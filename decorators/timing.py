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
            _start_time : float = time.perf_counter()
            _result : Any = func(*args, **kwargs)
            _end_time : float = time.perf_counter()
            _msg = f"<{func.__name__}> Processing Time: {end_time - start_time:.4f} sec."
            if self._logger:
                self._logger.info(_msg)
            elif not self._logger:
                print(_msg)
            else:
                raise Exception(f"You can see this exception message, when the type of `TimeDecorator.logger` is neither `logging.Logger` nor `None`.")
            return _result
        return wrapper


def stopwatch(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        # Note that timing your code once isn't the most reliable option
        # for timing your code. Look into the timeit module for more accurate
        # timing.
        start_time: float = perf_counter()
        result: Any = func(*args, **kwargs)
        end_time: float = perf_counter()

        print(f"<{func.__name__}> Processing Time: {end_time - start_time:.4f} sec.")
        return result

    return wrapper

sw = stopwatch
# Sample function 1
@sw
def connect() -> None:
    print('Connecting...')
    sleep(2)
    print('Connected!')


# Sample function 2
@sw
def fifty_million_loops() -> None:
    fifty_million: int = int(5e7)

    print('Looping...')
    for _ in range(fifty_million):
        pass

    print('Done looping!')


def main() -> None:
    fifty_million_loops()
    connect()


if __name__ == '__main__':
    main()