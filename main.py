"""
Solution to the single row sliding tile puzzle problem by searching
Search algorithms are based on the book Artificial Intelligence: A Modern
Approach (AIMA).
"""

from src.uninformed_search import UninformedSearch
from src.informed_search import InformedSearch

if __name__ == "__main__":
    print("Choose the type of search algorithm : \n")
    print("1: Uninformed Search (Uniform-cost search)")
    print("2: Informed Search (Greedy best-first search)")

    opt = int(input())

    if opt == 1:
        input_conf = input("Enter initial configuration : ")
        uninformed_search = UninformedSearch(input_conf)
        uninformed_search.uniform_cost()
    elif opt == 2:
        input_conf = input("Enter initial configuration : ")
        informed_search = InformedSearch(input_conf)
        informed_search.greedy_best_first()
    else:
        print("Invalid input")
