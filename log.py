import logging


class Log:
    _level = {
        "debug" : logging.DEBUG, 
        "info" : logging.INFO, 
        "error" : logging.ERROR, 
        "warn" : logging.WARN,
        "warning" : logging.WARNING,
        "critical" : logging.CRITICAL
    }

    def __init__(self, 
    name : str, 
    rootlevel : str = "debug", 
    filelevel : str = "debug", 
    streamlevel : str = "info",
    filefmt : str = r'%(asctime)s [%(name)s, line %(lineno)d] %(levelname)s: %(message)s',
    streamfmt : str = r'%(message)s') -> None:
        """
        :param name: The name of the python script.
        :type name: str
        :return: None
        """
        self.name = name
        # Root 
        self._logger = logging.getLogger(self.name)
        self._logger.setLevel(self._level[rootlevel])
        # File Handler
        file_handler = logging.FileHandler(f'logs/{self.name}.log', encoding='utf-8-sig')
        file_handler.setLevel(self._level[filelevel])
        file_handler.setFormatter(logging.Formatter(filefmt))
        self._logger.addHandler(file_handler)
        # Stream Handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(self._level[streamlevel])
        stream_handler.setFormatter(logging.Formatter(streamfmt))
        self._logger.addHandler(stream_handler)

    def debug(self, message : str) -> None:
        return self._logger.debug(msg=message)

    def info(self, message : str) -> None:
        return self._logger.info(msg=message)

    def error(self, message : str) -> None:
        return self._logger.error(msg=message)

    def warn(self, message : str) -> None:
        return self._logger.warn(msg=message)

    def warning(self, message : str) -> None:
        return self._logger.warning(msg=message)

    def critical(self, message : str) -> None:
        return self._logger.critical(msg=message)