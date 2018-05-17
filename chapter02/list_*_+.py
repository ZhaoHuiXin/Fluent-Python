# -*- coding=utf-8 -*-
#
# Copyright @ 2018 HuiXin Zhao
# create list contain list by list_comprehension. correct
board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
print(board)

# create above list style by *. fault
weird_board = [['_'] * 3] * 3
weird_board[1][2] = 'X'
print(weird_board)

# the error is essentially the same as the code below.
# the error reason : append the same object three times to a list
row = ['_'] * 3
weird_board_by_for = []
for i in range(3):
    weird_board_by_for.append(row)
weird_board_by_for[1][2] = "O"
print(weird_board_by_for)

# instead, the correct method is essentially like below.
# A list is created in each iteration as a new line appended to the board list
board_by_for = []
for i in range(3):
    row = ['_'] * 3
    board_by_for.append(row)
board_by_for[1][2] = "O"
print(board_by_for)
