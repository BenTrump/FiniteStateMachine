from FSM import *


def main():
    state = Context(StateOne())
    state.go_to_one()
    state.go_to_two()
    state.go_to_three()
    state.go_to_one()


if __name__ == "__main__":
    main()
