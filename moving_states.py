from state.state import State


class IdleState(State):

    def enter_state(self):
        print('зашел в состояние ожидания')
        self.logic_update()

    def exit_state(self):
        print('вышел из состояния ожидания')

    def logic_update(self):
        self.command = input()
        if self.command == 'jump':
            print('получил команду прыгать')
            self.state_machine.change_state(JumpState)
        elif self.command == 'attack':
            print('получил команду атаковать')
            self.state_machine.change_state(AttackState)
        else:
            print('введена неверная команда')
            self.logic_update()


class JumpState(State):

    def enter_state(self):
        print('зашел в состояние прыжка')
        self.logic_update()

    def exit_state(self):
        print('вышел из состояния прыжка')

    def logic_update(self):
        print('совершаю прыжок')
        self.state_machine.change_state(IdleState)


class AttackState(State):
    def enter_state(self):
        print('зашел в состояние атаки')
        self.logic_update()

    def exit_state(self):
        print('вышел из состояния атаки')

    def logic_update(self):
        print('совершаю атаку')
        self.state_machine.change_state(IdleState)
