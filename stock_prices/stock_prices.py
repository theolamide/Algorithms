#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit_arr = []

    def max_profit_reccursion(prices):
        starting_price = prices[0]
        if len(prices) > 1:
            for i in prices[1:]:
                # print(i)
                max_profit = i - starting_price
                max_profit_arr.append(max_profit)
                # print(max_profit)

            sub_array = prices[1:]
            return max_profit_reccursion(sub_array)
        else:
            pass

    max_profit_reccursion(prices)
    max_profit = max(max_profit_arr)
    print("max", max_profit)
    return max_profit


find_max_profit([10, 7, 5, 8, 11, 9])
# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
