"""
This module represents some classes for a simple word game.

There are a number of incomplete methods in the which you must implement to make fully functional.

About the game board!
The board's tiles are indexed from 1 to N, and the first square (1,1) is in the top left.
A tile may be replaced by another tile, hence only one tile may occupy a space at any one time.
"""

class LetterTile:
    """ This class is complete. You do not have to do anything to complete this class """
    def __init__(self, letter):
        self.letter = letter.lower()


    def get_letter(self):
        """ Returns the letter associatedd with this tile. """
        return self.letter

    def get_score(self):
        """ Returns the score asscoiated with the letter tile """
        return {
           'a' :  1,
           'b' :  2,
           'c' :  2,
           'd' :  3,
           'e' :  1,
           'f' :  3,
           'g' :  2,
           'h' :  3,
           'i' :  1,
           'j' :  3,
           'k' :  2,
           'l' :  3,
           'm' :  5,
           'n' :  3,
           'o' :  1,
           'p' :  2,
           'q' :  2,
           'r' :  3,
           's' :  1,
           't' :  1,
           'u' :  1,
           'v' :  3,
           'w' :  3,
           'x' :  5,
           'y' :  3,
           'z' :  5
         }[self.letter]


class GameBoard:
    """ This class represents the gameboard itself.
        You are requried to complete this class.
    """
    def __init__(self,width,height):
        """ The constructor for setting up the gameboard """
        self.width = width
        self.height = height
        self.board = [[LetterTile("-") for col in range(width)] for row in range(height)]

    def set_tile(self,x,y,tile):
        """ Places a tile at a location on the board. """
        self.board[x-1][y-1] = tile

    def get_tile(self,x,y):
        """ Returns the tile at a location on the board """
        return self.board[x-1][y-1]

    def remove_tile(self,x,y):
        """ Removes the tile from the board and returns the tile"""
        r_tile = self.get_tile(x,y)
        self.set_tile(x,y,LetterTile("-"))
        return r_tile

    def get_words(self):
        """ Retuns a list of the words on the board sorted in alphabetic order.

        """
        temp1 = ""
        temp2 = ""
        result_list = []


        # append all characters from row to row 
        for i in range(self.height):
            for j in range(self.width):
                temp1 += self.board[i][j].get_letter()
            # append an extra character "-" for extract the word easily
            temp1 += "-"
        
        # append all characters from column to column 
        for i in range(self.width):
            for j in range(self.height):
                temp2 += self.board[j][i].get_letter()
            # append an extra character "-" for extract the word easily
            temp2 += "-"

        temp = (temp1+temp2).split("-")

        for i in range(len(temp)):
            # any valid word has at least two characters
            if len(temp[i])>1:
                result_list.append(temp[i])

        return sorted(result_list)      # return a sorted list

    def top_scoring_words(self):
        """ Returns a list of the top scoring words.
            If there is a single word, then the function should return a single item list.
            If multilpe words share the highest score, then the list should contain the words sorted alphabetically.
        """
        words = self.get_words()
        scores_words_dict = {}
        scores_list = list(map (lambda x :(sum(map(lambda y : LetterTile(y).get_score(), x))),words))           # calculate the scores of all words
        top_score = max(scores_list)            # find the top scores

        for i in range(len(words)):
            if scores_words_dict.__contains__(scores_list[i]):
                scores_words_dict[scores_list[i]].append(words[i])
            else:
                scores_words_dict.update({scores_list[i]:[words[i]]})

        return scores_words_dict[top_score]

    def print_board(self):
        """ Prints a visual representation of the board
            Please use the - character for unused spaces
        """
        temp = str()
        for i in range(self.height):
            temp += " "+ "-"*4*self.width + "\n"
            for j in range(self.width):
                temp += " | "+self.board[i][j].get_letter()
            temp += " |\n"
        temp += " "+ "-"*4*self.width
        print(temp)

    def letters_placed(self):
        """ Returns a count of all letters currently on the board """
        word_count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j].get_letter() != "-":
                    word_count += 1
        return word_count

if __name__ == "__main__":
    """ This is just a sample for testing you might want to add your own tests here """
    # board = GameBoard(10,10);

    # d = LetterTile("d")
    # e = LetterTile("e")
    # m = LetterTile("m")
    # o = LetterTile("o")
    
    # board.set_tile(1,1,d)
    # board.set_tile(2,1,e)
    # board.set_tile(3,1,m)
    # board.set_tile(4,1,o)

    # print(board.get_words())
    # print(board.top_scoring_words())


    # print ("There are {} letters placed on the board.".format(board.letters_placed()))
    # board.print_board()

    # # Uncomment below once you have implemented get_words
    # print ("=== Words ===")
    # for word in board.get_words():
    #     print(word)

    # # Uncomment below once you have implmented top_scoring_words
    # print ("=== Top Scoring Words ===")
    # for word in board.top_scoring_words():
    #     print(word)



    #My own test
    board = GameBoard(10,10)

    a = LetterTile("a")
    b = LetterTile("b")
    d = LetterTile("d")
    m = LetterTile("m")
    t = LetterTile("t")
    o = LetterTile("o")
    l = LetterTile("l")
    e = LetterTile("e")
    s = LetterTile("s")
    z = LetterTile("z")
    p = LetterTile("p")
    n = LetterTile("n")
    v = LetterTile("v")

    board.set_tile(1,1,a)
    board.set_tile(1,2,d)
    board.set_tile(1,3,a)
    board.set_tile(1,4,m)
    board.set_tile(1,6,t)
    board.set_tile(2,4,o)
    board.set_tile(2,6,a)
    board.set_tile(3,1,s)
    board.set_tile(3,2,a)
    board.set_tile(3,3,n)
    board.set_tile(3,4,d)
    board.set_tile(3,6,b)
    board.set_tile(4,1,z)
    board.set_tile(4,4,l)
    board.set_tile(4,6,l)
    board.set_tile(5,1,z)
    board.set_tile(5,4,e)
    board.set_tile(5,5,v)
    board.set_tile(5,6,e)
    board.set_tile(6,1,p)

    board.get_words()
    board.print_board()

    # for word in board.get_words():
    #      print(word)

    # print("----------------------")
    # for word in board.top_scoring_words():
    #      print(word)
