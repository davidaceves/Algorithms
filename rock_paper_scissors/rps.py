#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  arr = []

  r = "rock"
  p = "paper"
  s = "scissors"

  if n == 1:
     arr = [[r], [p], [s]]
     
  elif n == 0:
    arr = [[]]
    
  return arr

rock_paper_scissors(1)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')