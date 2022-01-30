from typing import Callable

class Event:
    def __init__(self, callbacks):
        self.__callbacks = callbacks

    def add(self, callback: Callable):
        self.__callbacks.append(callback)

    def remove(self, callback: Callable):
        self.__callbacks.remove(callback)

class EventSource:
    def __init__(self):
        self.__callbacks = []
        self._event = Event(self.__callbacks)

    @property
    def event(self) -> Event:
        return self._event

    def notify_all(self):
        for callback in self.__callbacks:
            callback()
