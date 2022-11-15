import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')

  a = np.array([list[0:3], list[3:6], list[6:]], dtype=int)
  
  calculations = {}

  calculations['mean'] = [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), a.mean()]
  calculations['variance'] = [a.var(axis=0).tolist(), a.var(axis=1).tolist(), a.var()]
  calculations['standard deviation'] = [a.std(axis=0).tolist(), a.std(axis=1).tolist(), a.std()]
  calculations['max'] = [a.max(axis=0).tolist(), a.max(axis=1).tolist(), a.max()]
  calculations['min'] = [a.min(axis=0).tolist(), a.min(axis=1).tolist(), a.min()]
  calculations['sum'] = [a.sum(axis=0).tolist(), a.sum(axis=1).tolist(), a.sum()]

  return calculations