

class StateMachine:
    def __init__(self, starting_state):
        self.current_state = starting_state()
        self.current_state.get_state_machine(state_machine=self)
        self.current_state.enter_state()

    def change_state(self, new_state):
        self.current_state.exit_state()
        self.current_state = new_state()
        self.current_state.get_state_machine(state_machine=self)
        self.current_state.enter_state()
