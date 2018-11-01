import part3



board = part3.GameBoard(15,10)

board.set_tile(1,1, part3.LetterTile("t"))
board.set_tile(1,2, part3.LetterTile("e"))
board.set_tile(1,3, part3.LetterTile("s"))
board.set_tile(1,4, part3.LetterTile("t"))
board.set_tile(3,2, part3.LetterTile("f"))
board.set_tile(3,5, part3.LetterTile("h"))
board.set_tile(3,7, part3.LetterTile("o"))
board.set_tile(3,8, part3.LetterTile("m"))
board.set_tile(3,9, part3.LetterTile("f"))
board.set_tile(3,10, part3.LetterTile("g"))
board.set_tile(3,13, part3.LetterTile("b"))
board.set_tile(4,1, part3.LetterTile("o"))
board.set_tile(4,4, part3.LetterTile("h"))
board.set_tile(4,5, part3.LetterTile("a"))
board.set_tile(4,13, part3.LetterTile("a"))
board.set_tile(5,5, part3.LetterTile("p"))
board.set_tile(5,2, part3.LetterTile("o"))
board.set_tile(5,9, part3.LetterTile("o"))
board.set_tile(5,14, part3.LetterTile("l"))
board.set_tile(6,2, part3.LetterTile("p"))
board.set_tile(6,3, part3.LetterTile("e"))
board.set_tile(6,4, part3.LetterTile("e"))
board.set_tile(6,5, part3.LetterTile("p"))
board.set_tile(6,7, part3.LetterTile("i"))
board.set_tile(6,8, part3.LetterTile("d"))
board.set_tile(6,9, part3.LetterTile("k"))
board.set_tile(6,14, part3.LetterTile("a"))
board.set_tile(7,2, part3.LetterTile("s"))
board.set_tile(7,5, part3.LetterTile("y"))
board.set_tile(7,12, part3.LetterTile("b"))
board.set_tile(7,13, part3.LetterTile("a"))
board.set_tile(8,4, part3.LetterTile("f"))
board.set_tile(8,7, part3.LetterTile("w"))
board.set_tile(8,8, part3.LetterTile("o"))
board.set_tile(8,9, part3.LetterTile("w"))
board.set_tile(8,14, part3.LetterTile("l"))
board.set_tile(8,15, part3.LetterTile("a"))
board.set_tile(9,4, part3.LetterTile("u"))
board.set_tile(9,9, part3.LetterTile("e"))
board.set_tile(9,10, part3.LetterTile("z"))
board.set_tile(9,12, part3.LetterTile("h"))
board.set_tile(9,13, part3.LetterTile("i"))
board.set_tile(10,1, part3.LetterTile("w"))
board.set_tile(10,2, part3.LetterTile("a"))
board.set_tile(10,3, part3.LetterTile("s"))
board.set_tile(10,4, part3.LetterTile("h"))
board.set_tile(10,12, part3.LetterTile("e"))
board.set_tile(10,13, part3.LetterTile("o"))

print("==Test 1[非正方形 Board]==")
print("==Your Board==")
board.print_board()
print("\n==Test Board==")
print("test-----------\n---------------\n-f--h-omfg--b--\no--ha-------a--\n-o--p---o----l-\n-peep-idk----a-\n-s--y------ba--\n---f--wow----la\n---u---ez--hi--\nwash-------eo--")

print("== Your get_words==")  
for each in board.get_words():
	print(each)
print("== Test get_words [顺序无所谓]==")
word_list = ["test","omfg","ha","peep","idk","wow","ez","wash","ops","fuh","happy","ok","we","ba","la","ba","la","hi","he","io","eo"]
for each in word_list:
	print(each)
count = 0
wrong_list = []
for each in board.get_words():
	if each in word_list:
		count += 1
	else:
		wrong_list.append(each)
print("Your word list has {} words been matched with test word list with {} words in total.\n the Wrong words list is {}".format(count, len(word_list), wrong_list))

print("==Your Top Score Word==")
for each in board.top_scoring_words():
	print(each)
print("==Test Top Score Word [顺序是重要的]==")
print("happy\nomfg")

print("==Your Letters Placed==")

print(board.letters_placed())
print("== Test Letters Placed")
print("There are 48 letters placed on board\n\n")

board = part3.GameBoard(10,10)

board.set_tile(1,1, part3.LetterTile("t"))
board.set_tile(1,2, part3.LetterTile("e"))
board.set_tile(1,3, part3.LetterTile("s"))
board.set_tile(1,4, part3.LetterTile("t"))
board.set_tile(3,2, part3.LetterTile("f"))
board.set_tile(3,5, part3.LetterTile("h"))
board.set_tile(3,7, part3.LetterTile("o"))
board.set_tile(3,8, part3.LetterTile("m"))
board.set_tile(3,9, part3.LetterTile("f"))
board.set_tile(3,10, part3.LetterTile("g"))
board.set_tile(4,1, part3.LetterTile("o"))
board.set_tile(4,4, part3.LetterTile("h"))
board.set_tile(4,5, part3.LetterTile("a"))
board.set_tile(5,5, part3.LetterTile("p"))
board.set_tile(5,2, part3.LetterTile("o"))
board.set_tile(5,9, part3.LetterTile("o"))
board.set_tile(6,2, part3.LetterTile("p"))
board.set_tile(6,3, part3.LetterTile("e"))
board.set_tile(6,4, part3.LetterTile("e"))
board.set_tile(6,5, part3.LetterTile("p"))
board.set_tile(6,7, part3.LetterTile("i"))
board.set_tile(6,8, part3.LetterTile("d"))
board.set_tile(6,9, part3.LetterTile("k"))
board.set_tile(7,2, part3.LetterTile("s"))
board.set_tile(7,5, part3.LetterTile("y"))
board.set_tile(8,4, part3.LetterTile("f"))
board.set_tile(8,7, part3.LetterTile("w"))
board.set_tile(8,8, part3.LetterTile("o"))
board.set_tile(8,9, part3.LetterTile("w"))
board.set_tile(9,4, part3.LetterTile("u"))
board.set_tile(9,9, part3.LetterTile("e"))
board.set_tile(9,10, part3.LetterTile("z"))
board.set_tile(10,1, part3.LetterTile("w"))
board.set_tile(10,2, part3.LetterTile("a"))
board.set_tile(10,3, part3.LetterTile("s"))
board.set_tile(10,4, part3.LetterTile("h"))

print("==Test 2[正方形 Board]==")
print("==Your Board==")
board.print_board()
print("\n==Test Board==")
print("test------\n----------\n-f--h-omfg\no--ha-----\n-o--p---o-\n-peep-idk-\n-s--y-----\n---f--wow-\n---u----ez\nwash------")

print("== Your get_words==")  
for each in board.get_words():
	print(each)
print("== Test get_words [顺序无所谓]==")
word_list = ["test","omfg","ha","peep","idk","wow","ez","wash","ops","fuh","happy","ok","we",]
for each in word_list:
	print(each)
count = 0
wrong_list = []
for each in board.get_words():
	if each in word_list:
		count += 1
	else:
		wrong_list.append(each)
print("Your word list has {} words been matched with test word list with {} words in total.\n the Wrong words list is {}".format(count, len(word_list), wrong_list))

print("==Your Top Score Word==")
for each in board.top_scoring_words():
	print(each)
print("==Test Top Score Word [顺序是重要的]==")
print("happy\nomfg")

print("==Your Letters Placed==")

print(board.letters_placed())
print("== Test Letters Placed")
print("There are 36 letters placed on board")



