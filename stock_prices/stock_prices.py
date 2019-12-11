#!/usr/bin/python

import argparse

# init commit

# prices = [1050, 270, 1540, 3800, 2]
# 1050 270 1540 3800 2


# def find_max_profit(prices):
#     highest_price = max(prices)
#     new_list = prices[0:prices.index(highest_price)]
#     print(new_list)
#     # lowest_before = min(new_list, default=0)
#     # print(new_list)
#     lowest = highest_price

#     for i in new_list:
#         if i < lowest:
#             lowest = new_list[i]

#     # lowest_before = min(prices[:prices.index(highest_price)])
#     # print('find by index', prices.index(lowest_before))
#     # print('min', lowest_before)
#     print('min', lowest)

#     # find highest prices in list
#     # for i in prices:
#     #     print(i)

#     # for j in range(len(prices), -1, -1):

#     print('max', highest_price)

#     # return highest_price - lowest_before
#     return highest_price - lowest

# 100 90 80 50 20 10
def find_max_profit(prices):
    result = 0
    print(prices)
    highest_price = max(prices[1:])
    new_list = prices[0:prices.index(highest_price) + 1]
    print('new list', new_list)
    lowest_before = min(new_list)
    print('min', lowest_before)
    print('max', highest_price)
    print('result', highest_price - lowest_before)

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
