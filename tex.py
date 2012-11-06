from math import *

def makeRow(num,row):
  return num + " & " + row + "\\\\\n"

def ztable(l,s):
  body = [makeRow(str(x),str(y)) for (x,y) in zip(range(1,1 + len(l)), l)]
  numcols = 0
  if len(body) > 0: numcols = len(body[0].split('&'))
  if numcols == 0: return ''

  table = '\\begin{tabular}{|' + (numcols*'c|') + '}\n' + \
          '\\hline\n' + \
          'Trial & ' + s + '\n' + \
          '\\hline\n' + \
          ''.join(body) + \
          '\\hline\n' + \
          '\\end{tabular}\n'
  return table

def ztable_list(ls,s):
    return ztable([' & '.join(l) for l in ls],' & '.join(s))

def mean(l):
  return (1.0*sum(l))/len(l)

def variance(l):
  m = mean(l)
  return sum([(x-m)**2 for x in l])/len(l)

def stddev(l):
  return sqrt(variance(l))
