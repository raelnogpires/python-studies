# exercise 2
# you're developing new features to virtual assistant Alexa
# using the Observer pattern.
# when the alarm goes out, it will trigger a series of tasks to be done
# at home. (turn on lights, make coffee, turn on pc)

from abc import abstractmethod, ABC


class Alarm:
    def __init__(self) -> None:
        self._routines = []

    def create_new_routine(self, routine) -> None:
        self._routines.append(routine)

    def trigger_routines(self) -> None:
        for routine in self._routines:
            routine.activate()

    def wake_up(self):
        print("time to wake up!")
        self.trigger_routines()


# Observer interace
class Trigger(ABC):
    @abstractmethod
    def activate(self) -> None:
        ...


class LightsTrigger(Trigger):
    def __init__(self, alarm: Alarm) -> None:
        self._alarm = alarm
        self._alarm.create_new_routine(self)

    def activate(self) -> None:
        print("turning on lights.")


class CoffeeTrigger(Trigger):
    def __init__(self, alarm: Alarm) -> None:
        self._alarm = alarm
        self._alarm.create_new_routine(self)

    def activate(self) -> None:
        print("starting to make coffee, will be ready in 5 minutes.")


class PCTrigger(Trigger):
    def __init__(self, alarm: Alarm) -> None:
        self._alarm = alarm
        self._alarm.create_new_routine(self)

    def activate(self) -> None:
        print("turning on pc.")


if __name__ == "__main__":
    alarm = Alarm()
    LightsTrigger(alarm)
    CoffeeTrigger(alarm)
    PCTrigger(alarm)

    alarm.wake_up()
