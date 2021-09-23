from __future__ import annotations
from abc import ABC, abstractclassmethod
from typing import List, Dict

class IObservable(ABC):
    """ Observable """

    @property
    @abstractclassmethod
    def state(self):pass

    @abstractclassmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractclassmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractclassmethod
    def notify_observers(self) -> None: pass


class WeatherStation(IObservable):
    """ Observable """
    def __init__(self):
        self._observers:List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}
        if new_state != self._state:
            self._state = new_state
            self.notify_observers() 

    def reset_state(self):
        self._state = {}

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(
            observer
        )

    def remove_observer(self, observer: IObserver) -> None: 
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()
            print()

class IObserver(ABC):
    @abstractclassmethod
    def update(self) -> None: pass


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None: 
        observable_name = self.observable.__class__.__name__
        print(
            f"{self.name} o objeto {observable_name} acabou de atualizado => {self.observable.state}"
        )
        

if __name__ == "__main__":
    weather_station = WeatherStation()

    smartphone = Smartphone("IPhone", weather_station)
    outro_smartphone = Smartphone("Outro Smartphone", weather_station)

    weather_station.add_observer(smartphone)
    weather_station.add_observer(outro_smartphone)

    weather_station.state = {"temperature": "30"}
    weather_station.state = {"temperature": "30", "humidity": 90}


    weather_station.remove_observer(outro_smartphone)
    weather_station.reset_state()
