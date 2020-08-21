#!/usr/bin/python

import sys
#  0c 1c 2c 3c 3c 4c 4c 4c 4c 4c 5c 5c 5c 5c 5c  5c  5c  5c  5c  5c  5c  #coins
#  00 05 10 15 20 25 30 35 40 45 50 55 60 65 70  75  80  85  90  95  100 #total
#  01 02 04 06 09 13 18 24 31 39 49 62 77 93 112 134 159 187 218 253 292 #combos

def making_change(amount, denominations):
  # 1,5,10,25,50 denominations 
  answer = 1
  if amount <= 4 : return answer
  for i in range(4, -1, -1):
    print(denominations[i])
    if(amount == denominations[i]):
      answer += 1
      #if(amount <= denominations[i]):
        

  return 1

making_change(10, [1, 5, 10, 25, 50])

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")