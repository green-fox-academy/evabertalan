# def print_board(field):
#     field=([[1,1,0,1,0,0,1,1,1,1],
#         [0,0,0,1,0,0,0,0,0,0],
#         [1,0,0,1,0,1,1,1,0,1],
#         [1,0,0,0,0,0,0,0,0,1],
#         [1,0,0,0,0,0,0,0,0,0],
#         [1,0,0,0,0,1,0,0,0,1],
#         [0,0,0,0,0,1,0,0,0,1],
#         [1,1,0,0,0,0,0,0,0,1],
#         [0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,1,1,1,1,1,1]])
#     print(field)



# def find_ship:
#     for i in field:
#         if i == 1


#from random import randint

class CreateBoard:
    board = []
    for x in range(10):
        board.append(["O"] * 10)

    def print_board(board):
        for row in board:
            print (" ".join(row))

    print_board(board)

#def create_ship():
