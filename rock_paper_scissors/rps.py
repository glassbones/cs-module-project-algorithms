#!/usr/bin/python

import sys
import math

def dig(lists, n, value):
  if len(lists) == n: return lists.insert(0, value)
  for l in lists: dig(l, n, value)

def rpc(n):
  if n == 1: return [0],[1],[2]
  lists = [rpc(n-1) for i in range(3)]
  for insertValue, item in enumerate(lists):
    dig(item, n-1, insertValue)
  return lists


print('')
print('')
print('input = 1')
print(rpc(1))
print('')
print('')
print('input = 2')
print(rpc(2))
print('')
print('')
print('input = 3')
print(rpc(3))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')