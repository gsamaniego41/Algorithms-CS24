#!/usr/bin/python

import argparse


def find_max_profit(prices):
    result = 0
    print(prices)
    highest_price = max(prices[1:])
    new_list = prices[0:prices.index(highest_price) + 1]
    lowest_before = min(new_list)

    if len(new_list) < 3:
        result = new_list[1] - new_list[0]
    else:
        result = highest_price - lowest_before

    return result


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
