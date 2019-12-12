#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    outcomes = []

    # inner recursive function
    def find_outcomes(n, result):
        # print('result', result)
        # print('rounds', n)

        # base case
        if n == 0:
            print('result', result)
            # print('outcomes', outcomes)
            outcomes.append(result)
            return

        # recursive case
        # for play in plays:
        #     # outcomes.append(result)
        #     # collect plays * n in a list
        #     # count down to 0 to hit base case
        #     find_outcomes(n-1, result + [play])
        [find_outcomes(n-1, result + [play]) for play in plays]

    # initiate recursion
    find_outcomes(n, [])
    return outcomes


# print(rock_paper_scissors(2))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
