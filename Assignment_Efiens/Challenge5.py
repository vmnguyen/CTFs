'''

3 6
1 1 1 2
2 1 2 2
1 1 1 3
2 3 3 1
1 3 1 2
1 3 2 1
'''

N = 3
M = 6
test0 = "1 1 1 2"
test1 = "2 1 2 2"

test2 = "1 1 1 3"
test3 = "2 3 3 1"
test4 = "1 3 1 2"
test5 = "1 3 2 1"
board = []
for i in range(0,N):
	board.append(["O"]*N)


board[0][0] = '1'
for i in board:
	print " ".join(i)
a = test.split()
