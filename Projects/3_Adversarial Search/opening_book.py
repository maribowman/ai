import pickle
import random

import time

from isolation import Isolation
from my_custom_player import alpha_beta_search


def build_table(num_rounds=10):
    # Builds a table that maps from game state -> action
    # by choosing the action that accumulates the most
    # wins for the active player. (Note that this uses
    # raw win counts, which are a poor statistic to
    # estimate the value of an action; better statistics
    # exist.)
    from collections import defaultdict, Counter
    book = defaultdict(Counter)
    for _ in range(num_rounds):
        state = Isolation()
        build_tree(state, book)
    return {k: max(v, key=v.get) for k, v in book.items()}


def build_tree(state, book, depth=10):
    if depth <= 0 or state.terminal_test():
        return -simulate(state)
    action = alpha_beta_search(state=state, depth=5)
    reward = build_tree(state.result(action), book, depth - 1)
    book[state][action] += reward
    return -reward


def simulate(state):
    while not state.terminal_test():
        state = state.result(random.choice(state.actions()))
    return -1 if state.utility(state.player()) < 0 else 1


if __name__ == "__main__":
    rounds = 100
    start = time.time()
    open_book = build_table(rounds)
    end = time.time()
    print(
        f"The total time for {rounds} rounds is {end - start} seconds, the average time for each round is {((end - start) / rounds)} seconds per round")
    with open("data.pickle", 'wb') as f:
        pickle.dump(open_book, f)
