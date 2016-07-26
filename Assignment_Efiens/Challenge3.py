#!/usr/bin/python



def balance(lengh,count):
	return "0"*(lengh-len(str(count))) + str(count)

def print_Spiral(d):
	board = []
	for i in range(0,d):
		board.append(["O"] * d)

	count = d**2

	lengh = len(str(count))
	hangtren = 0
	hangduoi = d-1
	cottrai = 0
	cotphai = d-1

	while count >1:
		for j in range(cotphai, cottrai,-1):
			board[hangtren][j] = balance(lengh,count)
			count = count-1
			

		for j in range(hangtren, hangduoi):
			board[j][cottrai] = balance(lengh,count)
			count = count-1
		

		for j in range(cottrai, cotphai):
			board[hangduoi][j] = balance(lengh,count)
			count = count - 1
		
		for j in range(hangduoi,hangtren,-1):
			board[j][cotphai] = balance(lengh,count)
			count = count -1
		
		cottrai = cottrai +1
		hangduoi = hangduoi - 1
		hangtren = hangtren+1
		cotphai = cotphai - 1
		if count == 1:
			board[hangtren][cottrai] = balance(lengh,count)
			count = count -1

	print "="*18, "N =",d, "="*18
	for i in board:
		print " ".join(i)
		


for m in range(2,100):
	print_Spiral(m)




