import math
from jovian.pythondsa import evaluate_test_cases

#PROBLEM: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

tests = []
#0 query occurs in the middle
tests.append({
    'input' : {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})
#1 query is the first element
tests.append({
    'input' : {
        'cards' : [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})
#2 query is the last element
tests.append({
    'input' : {
        'cards' : [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})
#3 cards contains just one element
tests.append({
    'input' : {
        'cards' : [6],
        'query': 6
    },
    'output': 0
})
#4 cards does not contain query
tests.append({
    'input' : {
        'cards' : [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})
#5 cards is empty
tests.append({
    'input' : {
        'cards' : [],
        'query': 7
    },
    'output': -1
})
#6 numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})
#7 query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})
#large test
tests.append({
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
})

evaluate_test_cases(locate_card, tests)

