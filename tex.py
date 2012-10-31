from math import *

def makeRow(l):
  return " & ".join(map(lambda x: str(x),l)) + "\\\\\n"

def ztable(l,s):
  body = map(lambda x: makeRow(list(x)), zip(range(1,1 + len(l)), l))
  table = '\\begin{tabular}{|c|c|}\n' + '\\hline\n' + 'Trial & ' + s + '\n' + '\\hline\n' + ''.join(body) + '\\hline\n' + '\\end{tabular}\n'
  return table

def mean(l):
  return (1.0*sum(l))/len(l)

def variance(l):
  m = mean(l)
  return sum(map(lambda x: (x-m)**2, l))/len(l)

def stddev(l):
  return sqrt(variance(l))
