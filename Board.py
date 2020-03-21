import numpy as np


class Board:
    '''
    An instance represents a Sudoku Board.
    '''
    
    def __init__(self, f=None):
        '''
        Creates a new board.
        '''
        if f == None:
            self.board = np.zeros((9,9), dtype=int)
        else:
            self.board = np.loadtxt(f, dtype=int, delimiter=',')
        
    def get_value(self, i, j):
        '''
        Returns the value in the ith row and jth column.
        Requires: 0 <= i <= 8
                  0 <= j <= 8
        '''
        return self.board[i,j]

    def get_row(self, i):
        '''
        Returns the ith row.
        Requires: 0 <= i <= 8
        '''
        return self.board[i]
    
    def get_column(self, j):
        '''
        Returns the jth row.
        Requires: 0 <= j <= 8
        '''
        return self.board[:,j]
        
    def get_box(self, i, j):
        '''
        Returns the (i,j)th box.
        Requires: 0 <= i <= 2
                  0 <= j <= 2
        '''
        return self.board[3*i:3*i+3, 3*j:3*j+3]
        
    def set_value(self, i, j, v):
        '''
        Sets the (i,j)th value to v.
        Requires: 1 <= v <= 9
        	  0 <= i <= 8
        	  0 <= j <= 8
        '''
        self.board[i,j] = v
