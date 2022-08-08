# exercise 3
# create a log system by severity level
# (diagram received for developing this exercise)
from abc import ABC, abstractmethod
from datetime import datetime


class LogManipulator(ABC):
    @classmethod
    @abstractmethod
    def log(cls, msg):
        raise NotImplementedError


class TextLog(LogManipulator):
    @classmethod
    def log(cls, msg):
        with open("log_output.txt", "a") as file:
            print(msg, file=file)


class ScreenLog(LogManipulator):
    @classmethod
    def log(cls, msg):
        print(msg)


class Log:
    def __init__(self, manipulators):
        self.__manipulators = set(manipulators)

    def add_manipulator(self, manipulator):
        self.__manipulators.add(manipulator)

    def __format(self, lvl, msg):
        date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return f"[{date}][{lvl}] -> {msg}"

    def __log(self, lvl, msg):
        for m in self.__manipulators:
            formatted = self.__format(lvl, msg)
            m.log(formatted)

    def info(self, msg):
        self.__log("INFO: ", msg)

    def alert(self, msg):
        self.__log("ALERT: ", msg)

    def err(self, msg):
        self.__log("ERROR: ", msg)

    def debug(self, msg):
        self.__log("DEBUG: ", msg)
