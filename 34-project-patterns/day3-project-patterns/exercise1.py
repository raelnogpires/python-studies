red = "\033[91m"
green = "\033[92m"
orange = "\033[93m"
reset = "\033[0m"


class Log:
    def trigger_log(message: str) -> str:
        return message


class LogError:
    def __init__(self, logger: Log):
        self._log = logger

    def trigger_log(self, message: str) -> str:
        return f"{red}{self._log.trigger_log(message)}{reset}"


class LogWarning:
    def __init__(self, logger: Log):
        self._log = logger

    def trigger_log(self, message: str) -> str:
        return f"{orange}{self._log.trigger_log(message)}{reset}"


class LogSuccess:
    def __init__(self, logger: Log):
        self._log = logger

    def trigger_log(self, message: str) -> str:
        return f"{green}{self._log.trigger_log(message)}{reset}"


err = LogError(Log)
warn = LogWarning(Log)
success = LogSuccess(Log)

print(err.trigger_log("this is an error message"))
print(warn.trigger_log("this is a warning message"))
print(success.trigger_log("this is a success message"))
