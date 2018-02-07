from random import randint
import os
# x->ratat
# O-> neatins de nimic
# 1-> nava
# *->distrus
# in aux tin navele
# in board tin focurile
def createTable(size):
    boardGame=[]
    for i in range(0,size):
        line=["O"]*size
        boardGame.append(line)
        
    return boardGame

def customPrint(boardGame):
    ch=" "
    for line in boardGame:
        print (ch.join(line))


def makeCross(auxBoard):
    center_line=randint(1,len(auxBoard)-2)
    center_row=randint(1,len(auxBoard)-2)
    if auxBoard[center_line][center_row]!="1" and auxBoard[center_line][center_row+1]!="1" and auxBoard[center_line][center_row-1]!="1" and \
        auxBoard[center_line+1][center_row]!="1" and auxBoard[center_line-1][center_row]!="1" :

        auxBoard[center_line][center_row]="1"
        auxBoard[center_line][center_row-1]="1"
        auxBoard[center_line][center_row+1]="1"
        auxBoard[center_line-1][center_row]="1"
        auxBoard[center_line+1][center_row]="1"

def checkWin(boardGame,auxBoardGame):
    for line in range(0,len(boardGame)):
        for col in range(0,len(boardGame)):
            if auxBoardGame[line][col]=="1" and boardGame[line][col]=="O":
                return 0
    return 1
            

def maineGame(boardGame,auxBoardGame):

     for i in range(0,20):
         clear = lambda: os.system('cls')
         clear()
         print ("Turn %d" % (i+1))
         customPrint(boardGame)
         guess_row = int(input("Guess Row: "))
         guess_col = int(input("Guess Col: "))

         if guess_col<len(boardGame) and guess_row<len(boardGame):
             if(auxBoardGame[guess_row][guess_col]=="1"):
                 boardGame[guess_row][guess_col]="*"
                 if checkWin(boardGame,auxBoardGame)==1:
                     return 1
             else:
                 boardGame[guess_row][guess_col]="X"
         else:
             print ("Out of board game..")
         customPrint(boardGame)
     return 0

def main(boardGame,auxBoardGame):
     if maineGame(boardGame,auxBoardGame)==1:
        print("Congr! You win!")
     else:
         print ("Out of turns")


   
boardGame=createTable(6)
auxboard=createTable(6)
makeCross(auxboard)
makeCross(auxboard)
maineGame(boardGame,auxboard)
main(boardGame,auxBoardGame)
