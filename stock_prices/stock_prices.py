#!/usr/bin/python

import argparse

def find_max_profit(num):
  smallest_num = num[0] #starting num
  smallest_index = 0

  largest_num = 0
  cur_num_large = num[smallest_index + 1] # starting num large

  for i in range(0, len(num) - 2):
    next_index = i + 1

    if smallest_num > num[next_index]:
      smallest_num = num[next_index]
      smallest_index = next_index

  for j in range(smallest_index + 1, len(num)):
    cur_index = j

    if smallest_index == len(num) - 2:
      largest_num = num[len(num) - 1]

    if cur_num_large < num[cur_index]:
      cur_num_large = num[cur_index]
      largest_num = num[cur_index]

        
  
  return largest_num - smallest_num

 
find_max_profit([1050, 270, 1540, 3800, 2])
find_max_profit([10, 7, 5, 8, 11, 9])
find_max_profit([100, 90, 80, 50, 20, 10])
find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))