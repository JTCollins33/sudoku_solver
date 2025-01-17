from selenium import webdriver
import time
import numpy as np

DIM=9

BOARD = np.array([[0,0,8,0,0,0,0,6,0],
                  [4,2,9,0,0,0,1,8,0],
                  [0,0,1,2,0,0,3,7,0],
                  [8,0,0,0,0,1,0,0,0],
                  [7,0,0,0,6,0,0,0,0],
                  [1,0,6,0,0,2,7,5,3],
                  [0,0,7,0,0,0,0,0,9],
                  [0,0,0,7,0,0,5,0,1],
                  [6,0,3,4,0,5,0,0,0]])

def find_possibilities_of_set(set, possibilities, row, col):
    for n in set:
        if((n-1)>=0):
            possibilities[row,col,n-1]=0

def get_possible_matrix():
    m = np.zeros((9,9,9))
    for i in range(9):
        for j in range(9):
            for k in range(9):
                m[i,j,k]=k+1
    return m

def check_rows_and_columns(possibilities):
    for row in range(BOARD.shape[0]):
        for col in range(BOARD.shape[1]):
            find_possibilities_of_set(BOARD[row,:], possibilities, row, col)
            find_possibilities_of_set(BOARD[:,col], possibilities, row, col)

def check_squares(possibilities):
    for i in range(3):
        for j in range(3):
            square = BOARD[i:i*3,j:j*3]
            


if __name__=='__main__':
    possibilities = get_possible_matrix()
    check_rows_and_columns(possibilities)
    check_squares(possibilities)

    x=2