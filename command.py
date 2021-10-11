from abc import ABC, abstractmethod
from typing import List


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class Zealot:
    def charge(self):
        print("за айур!")

    def move(self):
        print("выдвигаюсь")


class Probe:
    def build(self):
        print("создаю портал")


class ChargeCommand(Command):
    def __init__(self, executor: Zealot):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.charge()
        self.__executor.move()


class СonstructionCommand(Command):
    def __init__(self, executor: Probe):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.build()


class OccupationCommand(Command):
    def __init__(self, builder: Probe, attacker: Zealot):
        self.__builder = builder
        self.__attacker = attacker

    def execute(self) -> None:
        self.__builder.build()
        self.__builder.build()
        self.__attacker.charge()



class Invoker:
    def __init__(self):
        self.pattern: List[Command] = []

    def addCommand(self, command: Command) -> None:
        self.pattern.append(command)

    def play(self) -> None:
        if self.pattern:
            for executor in self.pattern:
                executor.execute()
        else:
            print('не задана последовательность действий')
        self.pattern.clear()


if __name__ == "__main__":
    zealot = Zealot()
    probe = Probe()
    player = Invoker()

    player.addCommand(ChargeCommand(zealot))
    player.addCommand(СonstructionCommand(probe))
    player.addCommand(OccupationCommand(probe, zealot))
    player.play()
