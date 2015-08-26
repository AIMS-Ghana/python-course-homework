#!/usr/bin/python

import os

X = 'X'
O = 'O'
EMP = ""
TIE = 'TIE'
NUM_SQ = 9

# Rules for the game
def rules():
    print """This is the tic tac toe game."""

# Ask a question   
def ask(ques):
      res = None
      while res not in ('y', 'n'):
           res = raw_input(ques)
      return res



#functin to decide moves  
def hand():
      go_1st = ask('Do you want to move first\t')
      if go_1st == 'y':
          human = X
          comp = O
      else:
          human = O
          comp = X
      return comp, human


# function to creat a new board
def new_board(): 
    board = []
    for sq in range(NUM_SQ):
        board.append(EMP) 
    return board  
      
# function to display board      
def dis_board(board):
      print "\n\t", board[0], "|", board[1], "|", board[2]
      print "\t", "______"
      print "\t", board[3], "|", board[4], "|", board[5]
      print "\t", "______"
      print "\t", board[6], "|", board[7], "|", board[8], "\n" 
      
      
#Legal moves or moves that has already taken place
def legal_move(board):
     mv = []
     for sq in range(NUM_SQ):
         if board[sq] == EMP:
             mv.append(sq)
     return mv
     
     
#function to ask for a box number
def box_num(q, l, h):
    res = None
    while res not in range(l, h):
          res = int(raw_input(q))
    return res          
     
# Human move function      
def human_move(b, h):
    l_mv = legal_move(b) 
    mv = None
    while mv not in l_mv:
          mv = box_num(" Enter numbers between (0-8) to make a move.\n The legal moves are" + str(legal_move(b))+"\t ###\t", 0, NUM_SQ)
    return mv 
    
# Copmuter move function
def comp_move(b, comp, h):
     b = b[:]
     
   # Logic here allows the computer to win
     for mv in legal_move(b):
         b[mv] = comp
         if win_bd(b) == comp:
             print mv
             return mv
         b[mv] = EMP
     
     
   # Logic here allows the computer to prevent the human from winning nex move
     for mv in legal_move(b):
          b[mv] = h
          if win_bd(b) == h:
              print mv
              return mv
          b[mv] = EMP

   # Logic here make the computer takes the best move 
   #       if the above two logic don't work'
     for mv in (4, 0, 2, 6, 8, 1, 3, 5, 7):
           if mv in legal_move(b):
               print mv
               return mv
               
          
#dis_board(new_board())      
 
# function to determine winner
def win_bd(b):
    win_pos = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) 
    for row in win_pos:
        if b[row[0]] == b[row[1]] == b[row[2]] != EMP:
            winner = b[row[0]]
            return winner
    if EMP not in b:
       return TIE 
       

def msg_for_winner(the_winner, c, h):
     if the_winner != TIE: print "WOW", the_winner, "WON !!!\n"
     else: 
         print "A TIE !!!\n"
     
     #if the_winner == h:
        #print""
          


# This fuction is to switch turns
def whose_turn(turn):
    if turn == X: return O
    else: return X 
    
    
# start of game      
def main():
    rules()
    comp, human = hand()
    turn = X
    b = new_board()
    dis_board(b)
    
    while not win_bd(b):
         os.system('clear')
         dis_board(b)
         if turn == human:  
             mv = human_move(b, human)
             b[mv] = human
         else: 
              mv = comp_move(b, comp, human)
              b[mv] = comp
         turn = whose_turn(turn)
          
    dis_board(b)      
    the_winner = win_bd(b)
    
    msg_for_winner(the_winner, comp, human)
                     
main()         
           
              
              
    
    
 
      
      

      
      
      
      
