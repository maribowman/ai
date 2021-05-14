import pickle
import random
from collections import defaultdict, Counter

from math import trunc

from isolation import Isolation, DebugState

ROUNDS = 10
DEPTH = 4


def build_table():
    book = defaultdict(Counter)
    state = Isolation()
    build_tree(state, book, DEPTH)
    return {k: max(v, key=v.get) for k, v in book.items()}


def build_tree(state, book, depth):
    if depth <= 0 or state.terminal_test():
        return -simulate(state)

    total_score = 0
    for index, action in enumerate(state.actions()):
        score = build_tree(state.result(action), book, depth - 1)
        book[state][action] += score
        total_score += score
        if depth == DEPTH:
            print(f"{trunc((index + 1) / len(state.actions()) * 100)}%")
    return -total_score


def simulate(state):
    score = 0
    for _ in range(ROUNDS):
        current_state = state
        player_id = current_state.player()
        while not current_state.terminal_test():
            current_state = current_state.result(random.choice(current_state.actions()))
        score += -1 if current_state.utility(player_id) < 0 else 1
    return score


if __name__ == "__main__":
    book = build_table()

    with open("data2.pickle", 'wb') as f:
        pickle.dump(book, f)

    bench_game = Isolation()
    best_opening = book[bench_game]
    print("Best opening move: {}".format(DebugState.ind2xy(best_opening)))
    result = bench_game.result(best_opening)
    best_response = book[result]
    print(f"best response: {DebugState.ind2xy(best_response)}")
