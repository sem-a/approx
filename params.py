import numpy as np

def set_h(temp): 
    global _h 
    _h = temp

def set_mu(temp): 
    global _mu 
    _mu = temp

def set_cell(temp): 
    global _cell_size
    _cell_size = temp

def get_h(): 
    global _h 
    return _h

def get_mu(): 
    global _mu 
    return _mu

def get_cell(): 
    global _cell_size
    return _cell_size

def get_n():
    global _n 
    return _n

_segment = np.array([0, 10])
_h = 0.001 # шаг
_mu = 0.1 # параметр
_n = int( (_segment[1] - _segment[0]) / _h )

_cell_size = 1.02 # размер клетки

