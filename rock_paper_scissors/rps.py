#!/usr/bin/python

import sys
import math


def change(n):
  if n != 3:return n + 1
  else: return 1

def makeList(n):
  l = []
  while (n > 0):
    l.append(change(n))
    n-= 1
  return l

def rock_paper_scissors(n):
  lists = {}
  l = []
  power = (3 ** n)
  while(power > 0):
    print(f'{power}')
    lists.update( {f'l{power}' : makeList(n)} )
    power -= 1

  return str(lists.values())[12:-1]


print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')