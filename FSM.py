import abc


class Context:
    def __init__(self, state):
        self._state = state

    def go_to_one(self):
        self._state.state_one()
        self._state = StateOne()

    def go_to_two(self):
        self._state.state_two()
        self._state = StateTwo()

    def go_to_three(self):
        self._state.state_three()
        self._state = StateThree()


class State(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def state_one(self):
        print("abstract state_one")
        pass

    @abc.abstractmethod
    def state_two(self):
        print("abstract state_two")
        pass

    @abc.abstractmethod
    def do_task_a(self):
        pass


class StateOne(State):
    def state_one(self):
        print("StateOne > StateOne")

    def state_two(self):
        print("StateOne > StateTwo")

    def state_three(self):
        print("StateOne > StateThree")


class StateTwo(State):
    def state_one(self):
        print("StateTwo > StateOne")

    def state_two(self):
        print("StateTwo > StateTwo")

    def state_three(self):
        print("StateTwo > StateThree")


class StateThree(State):
    def state_one(self):
        print("StateThree > StateOne")

    def state_two(self):
        print("StateThree > StateTwo")

    def state_three(self):
        print("StateThree > StateThree")
