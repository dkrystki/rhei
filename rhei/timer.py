import time
from enum import Enum


class EventType(Enum):
    INIT = 0
    START = 1
    PAUSE = 2
    REVERSE = 3
    STOP = 4
    RESET = 5


class Event:
    event_type: EventType = EventType.INIT

    def __init__(self, timer: "Timer", time_value: float = 0.0) -> None:
        self._time_value: float = time_value
        self._timer: "Timer" = timer
        self._create_timestamp: float = float(time.time())
        self._finished = False

    def finish(self) -> None:
        self._finished = True
        self._time_value = self._calculate_time()

    def get_time(self) -> float:
        return self._time_value if self._finished else self._calculate_time()

    def _calculate_time(self) -> float:
        return self._time_value


class InitEvent(Event):
    event_type: EventType = EventType.INIT


class StartEvent(Event):
    event_type: EventType = EventType.START

    def _calculate_time(self) -> float:
        return (
            self._time_value
            + self._timer.prev_event.get_time()
            + float(time.time())
            - self._create_timestamp
        )


class PauseEvent(Event):
    event_type: EventType = EventType.PAUSE

    def _calculate_time(self) -> float:
        return self._time_value + self._timer.prev_event.get_time()


class StopEvent(Event):
    event_type: EventType = EventType.STOP

    def _calculate_time(self) -> float:
        return 0.0


class ReverseEvent(Event):
    event_type: EventType = EventType.REVERSE

    def _calculate_time(self) -> float:
        return (
            self._time_value
            + self._timer.prev_event.get_time()
            - float(time.time() - self._create_timestamp)
        )


class ResetEvent(Event):
    event_type: EventType = EventType.RESET

    def _calculate_time(self) -> float:
        return self._time_value + float(time.time()) - self._create_timestamp


class TimerState(Enum):
    COUNTING = 1
    PAUSED = 2


class Timer:
    def __init__(self, initial_value: float = 0.0) -> None:
        self.prev_event: Event = InitEvent(self)
        self.curr_event: Event = InitEvent(self, time_value=initial_value)
        self._state: TimerState = TimerState.PAUSED
        self._initial_value = initial_value

    @property
    def state(self) -> TimerState:
        return self._state

    def _new_event(self, event: Event) -> None:
        self.curr_event.finish()
        self.prev_event = self.curr_event
        self.curr_event = event

    def start(self, reversed: bool = False) -> None:
        self._state = TimerState.COUNTING

        if reversed:
            self._new_event(ReverseEvent(self))
        else:
            self._new_event(StartEvent(self))

    def pause(self) -> None:
        self._state = TimerState.PAUSED
        self._new_event(PauseEvent(self))

    def stop(self) -> None:
        self.pause()
        self.reset()

    def reset(self, value: float = 0.0) -> None:
        self._new_event(ResetEvent(self, time_value=value))

    def get(self) -> float:
        return self.curr_event.get_time()
