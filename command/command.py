from __future__ import annotations
from typing import Dict, List, Tuple
from abc import ABC, abstractclassmethod

class Light:
    """ Receiver - Luz inteligente. """
    def __init__(self, name:str, room_name:str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = "Default color"
    
    def on(self):
        print(f"{self.name} no {self.room_name} está ON.")
    
    def off(self):
        print(f"{self.name} no {self.room_name} está OFF.")
    
    def change_color(self, color: Str ) -> None:
        self.color = color
        print(f"{self.name} no {self.room_name} está {self.color}.")


class ICommand(ABC):

    @abstractclassmethod
    def execute(self) -> None: pass

    @abstractclassmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None: 
        self.light.on()

    def undo(self) -> None:
        self.light.off()

class LightChangeColorCommand(ICommand):

    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    """Invoker"""

    def __init__(self) -> None:
        self._buttons: Dict[Str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []
        
    def button_add_command(self, name:str, command:ICommand ) -> None:
        self._buttons[name] = command
        
        
    def button_execute(self, name:str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name, "execute"))

    def button_undo(self, name:str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, "undo"))
    
    def global_undo(self):
        if not self._undos:
            return None
        
        button_name, action = self._undos[-1]

        if action == "execute":
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute() 
        
        self._undos.pop()

    
if __name__ == "__main__":
    bedroom_light = Light("Luz do quarto", "Quarto")
    bathroom_light = Light("Luz do banheiro", "Banheiro")

    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColorCommand(bedroom_light, "Blue")
    bedroom_light_red = LightChangeColorCommand(bedroom_light, "Red")

    remote = RemoteController()
    remote.button_add_command("First Button", bedroom_light_on)
    remote.button_add_command("Second Button", bathroom_light_on)
    remote.button_add_command("Third Button", bedroom_light_blue)
    remote.button_add_command("Four Button", bedroom_light_red)

    remote.button_execute("First Button")
    remote.button_execute("Second Button")
    remote.button_execute("Third Button")
    remote.button_undo("Third Button")
    remote.button_execute("Four Button")

    print()

    remote.global_undo()