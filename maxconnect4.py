#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
from MaxConnect4Game import *

def oneMoveGame(currentGame):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)

    currentGame.aiPlay() # Make a move

    print 'Game state after move:'
    currentGame.printGameBoard()

    currentGame.player1Score, currentGame.player2Score = countScore(currentGame.gameBoard)
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame, player):
    # Added Code
    while True:
        if currentGame.pieceCount == 42:    # Is the board full already?
            print 'BOARD FULL\n\nGame Over!\n'
            sys.exit(0)
        if player == 'computer-next': # AI's Turn
            currentGame.aiPlay()
            currentGame.gameFile = open('computer.txt','w')
            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()
            player = 'human-next'
        else:
            while True:
                print('Enter the column to play the next move: ')
                col = int(input())
                col-=1
                if col>=0 & col<=6:
                    result = currentGame.playPiece(col)
                    if result:
                        break
                print 'Invald Column. Enter Again\n'
            if currentGame.currentTurn == 1:
                currentGame.currentTurn = 2
            elif currentGame.currentTurn == 2:
                currentGame.currentTurn = 1
            currentGame.gameFile = open('human.txt','w')
            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()
            player = 'computer-next'
        # Print game and score
        currentGame.printGameBoard()
        currentGame.player1Score, currentGame.player2Score = countScore(currentGame.gameBoard)
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    
def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile= argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.player1Score, currentGame.player2Score = countScore(currentGame.gameBoard)
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    depth = int(argv[4])
    currentGame.depth_level = depth
    if game_mode == 'interactive':
        player= argv[3]
        interactiveGame(currentGame, player) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)



