"""
Given an list of integers as input. Print square of each element in this list. [1,7,9,12]
"""

def Squares(n):
  return n*n

ls = [1,7,9,12]
ln = len(ls)
for i in range(0,ln):
  e = ls[i]
  sqs = Squares(e)
  print(sqs)
  