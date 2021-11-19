import random

coordinates = {}
coordinates[1] = [1,1]
coordinates[2] = [2,1]
coordinates[3] = [3,1]

coordinates[4] = [1,2]
coordinates[5] = [2,2]
coordinates[6] = [2,3]

coordinates[7] = [1,3]
coordinates[8] = [2,3]
coordinates[9] = [3,3]

board = {'1': ' ' ,'2': ' ', '3': ' ',
         '4': ' ' ,'5': ' ', '6': ' ',
         '7': ' ' ,'8': ' ', '9': ' '}
def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

while(True):
    x = int(input("Enter a coordinate (1-9): "))
    if(board[x]

