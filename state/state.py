from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    def get_state_machine(self, state_machine):
        self.state_machine = state_machine

    @abstractmethod
    def enter_state(self):
        pass

    @abstractmethod
    def exit_state(self):
        pass

    @abstractmethod
    def logic_update(self):
        pass

