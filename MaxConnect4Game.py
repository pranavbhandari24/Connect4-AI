#!/usr/bin/env python

from copy import copy
import random
import sys

# Calculate the number of 4-in-a-row each player has
def countScore(Board):
    player1Score = 0
    player2Score = 0

    # Check horizontally
    for row in Board:
        # Check player 1
        if row[0:4] == [1]*4:
            player1Score += 1
        if row[1:5] == [1]*4:
            player1Score += 1
        if row[2:6] == [1]*4:
            player1Score += 1
        if row[3:7] == [1]*4:
            player1Score += 1
        # Check player 2
        if row[0:4] == [2]*4:
            player2Score += 1
        if row[1:5] == [2]*4:
            player2Score += 1
        if row[2:6] == [2]*4:
            player2Score += 1
        if row[3:7] == [2]*4:
            player2Score += 1

    # Check vertically
    for j in range(7):
        # Check player 1
        if (Board[0][j] == 1 and Board[1][j] == 1 and
                Board[2][j] == 1 and Board[3][j] == 1):
            player1Score += 1
        if (Board[1][j] == 1 and Board[2][j] == 1 and
                Board[3][j] == 1 and Board[4][j] == 1):
            player1Score += 1
        if (Board[2][j] == 1 and Board[3][j] == 1 and
                Board[4][j] == 1 and Board[5][j] == 1):
            player1Score += 1
        # Check player 2
        if (Board[0][j] == 2 and Board[1][j] == 2 and
                Board[2][j] == 2 and Board[3][j] == 2):
            player2Score += 1
        if (Board[1][j] == 2 and Board[2][j] == 2 and
                Board[3][j] == 2 and Board[4][j] == 2):
            player2Score += 1
        if (Board[2][j] == 2 and Board[3][j] == 2 and
                Board[4][j] == 2 and Board[5][j] == 2):
            player2Score += 1

    # Check diagonally

    # Check player 1
    if (Board[2][0] == 1 and Board[3][1] == 1 and
            Board[4][2] == 1 and Board[5][3] == 1):
        player1Score += 1
    if (Board[1][0] == 1 and Board[2][1] == 1 and
            Board[3][2] == 1 and Board[4][3] == 1):
        player1Score += 1
    if (Board[2][1] == 1 and Board[3][2] == 1 and
            Board[4][3] == 1 and Board[5][4] == 1):
        player1Score += 1
    if (Board[0][0] == 1 and Board[1][1] == 1 and
            Board[2][2] == 1 and Board[3][3] == 1):
        player1Score += 1
    if (Board[1][1] == 1 and Board[2][2] == 1 and
            Board[3][3] == 1 and Board[4][4] == 1):
        player1Score += 1
    if (Board[2][2] == 1 and Board[3][3] == 1 and
            Board[4][4] == 1 and Board[5][5] == 1):
        player1Score += 1
    if (Board[0][1] == 1 and Board[1][2] == 1 and
            Board[2][3] == 1 and Board[3][4] == 1):
        player1Score += 1
    if (Board[1][2] == 1 and Board[2][3] == 1 and
            Board[3][4] == 1 and Board[4][5] == 1):
        player1Score += 1
    if (Board[2][3] == 1 and Board[3][4] == 1 and
            Board[4][5] == 1 and Board[5][6] == 1):
        player1Score += 1
    if (Board[0][2] == 1 and Board[1][3] == 1 and
            Board[2][4] == 1 and Board[3][5] == 1):
        player1Score += 1
    if (Board[1][3] == 1 and Board[2][4] == 1 and
            Board[3][5] == 1 and Board[4][6] == 1):
        player1Score += 1
    if (Board[0][3] == 1 and Board[1][4] == 1 and
            Board[2][5] == 1 and Board[3][6] == 1):
        player1Score += 1

    if (Board[0][3] == 1 and Board[1][2] == 1 and
            Board[2][1] == 1 and Board[3][0] == 1):
        player1Score += 1
    if (Board[0][4] == 1 and Board[1][3] == 1 and
            Board[2][2] == 1 and Board[3][1] == 1):
        player1Score += 1
    if (Board[1][3] == 1 and Board[2][2] == 1 and
            Board[3][1] == 1 and Board[4][0] == 1):
        player1Score += 1
    if (Board[0][5] == 1 and Board[1][4] == 1 and
            Board[2][3] == 1 and Board[3][2] == 1):
        player1Score += 1
    if (Board[1][4] == 1 and Board[2][3] == 1 and
            Board[3][2] == 1 and Board[4][1] == 1):
        player1Score += 1
    if (Board[2][3] == 1 and Board[3][2] == 1 and
            Board[4][1] == 1 and Board[5][0] == 1):
        player1Score += 1
    if (Board[0][6] == 1 and Board[1][5] == 1 and
            Board[2][4] == 1 and Board[3][3] == 1):
        player1Score += 1
    if (Board[1][5] == 1 and Board[2][4] == 1 and
            Board[3][3] == 1 and Board[4][2] == 1):
        player1Score += 1
    if (Board[2][4] == 1 and Board[3][3] == 1 and
            Board[4][2] == 1 and Board[5][1] == 1):
        player1Score += 1
    if (Board[1][6] == 1 and Board[2][5] == 1 and
            Board[3][4] == 1 and Board[4][3] == 1):
        player1Score += 1
    if (Board[2][5] == 1 and Board[3][4] == 1 and
            Board[4][3] == 1 and Board[5][2] == 1):
        player1Score += 1
    if (Board[2][6] == 1 and Board[3][5] == 1 and
            Board[4][4] == 1 and Board[5][3] == 1):
        player1Score += 1

    # Check player 2
    if (Board[2][0] == 2 and Board[3][1] == 2 and
            Board[4][2] == 2 and Board[5][3] == 2):
        player2Score += 1
    if (Board[1][0] == 2 and Board[2][1] == 2 and
            Board[3][2] == 2 and Board[4][3] == 2):
        player2Score += 1
    if (Board[2][1] == 2 and Board[3][2] == 2 and
            Board[4][3] == 2 and Board[5][4] == 2):
        player2Score += 1
    if (Board[0][0] == 2 and Board[1][1] == 2 and
            Board[2][2] == 2 and Board[3][3] == 2):
        player2Score += 1
    if (Board[1][1] == 2 and Board[2][2] == 2 and
            Board[3][3] == 2 and Board[4][4] == 2):
        player2Score += 1
    if (Board[2][2] == 2 and Board[3][3] == 2 and
            Board[4][4] == 2 and Board[5][5] == 2):
        player2Score += 1
    if (Board[0][1] == 2 and Board[1][2] == 2 and
            Board[2][3] == 2 and Board[3][4] == 2):
        player2Score += 1
    if (Board[1][2] == 2 and Board[2][3] == 2 and
            Board[3][4] == 2 and Board[4][5] == 2):
        player2Score += 1
    if (Board[2][3] == 2 and Board[3][4] == 2 and
            Board[4][5] == 2 and Board[5][6] == 2):
        player2Score += 1
    if (Board[0][2] == 2 and Board[1][3] == 2 and
            Board[2][4] == 2 and Board[3][5] == 2):
        player2Score += 1
    if (Board[1][3] == 2 and Board[2][4] == 2 and
            Board[3][5] == 2 and Board[4][6] == 2):
        player2Score += 1
    if (Board[0][3] == 2 and Board[1][4] == 2 and
            Board[2][5] == 2 and Board[3][6] == 2):
        player2Score += 1

    if (Board[0][3] == 2 and Board[1][2] == 2 and
            Board[2][1] == 2 and Board[3][0] == 2):
        player2Score += 1
    if (Board[0][4] == 2 and Board[1][3] == 2 and
            Board[2][2] == 2 and Board[3][1] == 2):
        player2Score += 1
    if (Board[1][3] == 2 and Board[2][2] == 2 and
            Board[3][1] == 2 and Board[4][0] == 2):
        player2Score += 1
    if (Board[0][5] == 2 and Board[1][4] == 2 and
            Board[2][3] == 2 and Board[3][2] == 2):
        player2Score += 1
    if (Board[1][4] == 2 and Board[2][3] == 2 and
            Board[3][2] == 2 and Board[4][1] == 2):
        player2Score += 1
    if (Board[2][3] == 2 and Board[3][2] == 2 and
            Board[4][1] == 2 and Board[5][0] == 2):
        player2Score += 1
    if (Board[0][6] == 2 and Board[1][5] == 2 and
            Board[2][4] == 2 and Board[3][3] == 2):
        player2Score += 1
    if (Board[1][5] == 2 and Board[2][4] == 2 and
            Board[3][3] == 2 and Board[4][2] == 2):
        player2Score += 1
    if (Board[2][4] == 2 and Board[3][3] == 2 and
            Board[4][2] == 2 and Board[5][1] == 2):
        player2Score += 1
    if (Board[1][6] == 2 and Board[2][5] == 2 and
            Board[3][4] == 2 and Board[4][3] == 2):
        player2Score += 1
    if (Board[2][5] == 2 and Board[3][4] == 2 and
            Board[4][3] == 2 and Board[5][2] == 2):
        player2Score += 1
    if (Board[2][6] == 2 and Board[3][5] == 2 and
            Board[4][4] == 2 and Board[5][3] == 2):
        player2Score += 1
    return player1Score, player2Score

class maxConnect4Game:
    def __init__(self):
        self.gameBoard = [[0 for i in range(7)] for j in range(6)]
        self.currentTurn = 1
        self.player1Score = 0
        self.player2Score = 0
        self.pieceCount = 0
        self.depth_level = 0
        self.gameFile = None
        random.seed()

    # Count the number of pieces already played
    def checkPieceCount(self):
        self.pieceCount = sum(1 for row in self.gameBoard for piece in row if piece)

    # Output current game status to console
    def printGameBoard(self):
        print ' -----------------'
        for i in range(6):
            print ' |',
            for j in range(7):
                print('%d' % self.gameBoard[i][j]),
            print '| '
        print ' -----------------'

    # Output current game status to file
    def printGameBoardToFile(self):
        for row in self.gameBoard:
            self.gameFile.write(''.join(str(col) for col in row) + '\r\n')
        self.gameFile.write('%s\r\n' % str(self.currentTurn))

    # Place the current player's piece in the requested column
    def playPiece(self, column):
        if not self.gameBoard[0][column]:
            for i in range(5, -1, -1):
                if not self.gameBoard[i][column]:
                    self.gameBoard[i][column] = self.currentTurn
                    self.pieceCount += 1
                    return 1

    def utility_value(self, tempBoard):
        score1, score2 = countScore(tempBoard)
        if self.currentTurn == 1:
            return score1 - score2
        else:
            return score2 - score1
    
    def min_value(self, tempBoard, virtual_pieceCount, depth, alpha, beta):
        # Terminal Node or Depth level reached then return utility value
        if ((virtual_pieceCount == 42) or (depth==self.depth_level)):
            return self.utility_value(tempBoard)
        
        min = sys.maxint
        opponent_turn = 1 if self.currentTurn==2 else 2
        # For all actions finding the min of max_value
        for i in range(7):
            if not self.gameBoard[0][i]:
                tempBoard1 = [row[:] for row in tempBoard]
                for j in range(5, -1, -1):
                    if not tempBoard1[j][i]:
                        tempBoard1[j][i] = opponent_turn
                        break
                value = self.max_value(tempBoard1, virtual_pieceCount+1, depth+1, alpha, beta)
                if value < min:
                    min = value
                if min <= alpha:
                    return min
                beta = min if min < beta else beta
        return min

    def max_value(self, tempBoard, virtual_pieceCount, depth, alpha, beta):
        # Terminal Node or Depth level reached then return utility value
        if ((virtual_pieceCount == 42) or (depth==self.depth_level)):
            return self.utility_value(tempBoard)

        max = -sys.maxint -1
        for i in range(7):
            if not self.gameBoard[0][i]:
                tempBoard1 = [row[:] for row in tempBoard]
                for j in range(5, -1, -1):
                    if not tempBoard1[j][i]:
                        tempBoard1[j][i] = self.currentTurn
                        break
                value = self.min_value(tempBoard1, virtual_pieceCount+1, depth+1, alpha, beta)
                if value > max:
                    max = value
                if max >= beta:
                    return max
                alpha = max if max > alpha else alpha
        return max

    def minimax(self, virtual_pieceCount, alpha, beta):
        max =  -sys.maxint -1
        col = -1
        depth = 1
        for i in range(7):
            if not self.gameBoard[0][i]:
                tempBoard = [row[:] for row in self.gameBoard]
                for j in range(5, -1, -1):
                    if not tempBoard[j][i]:
                        tempBoard[j][i] = self.currentTurn
                        break
                value = self.min_value(tempBoard, virtual_pieceCount+1, depth, alpha, beta)
                if value > max:
                    max = value
                    col = i
        return col

    # The AI section. Currently plays randomly.
    def aiPlay(self):
        # Implement Alpha-Beta Pruned Minimax here
        # randColumn = random.randrange(0,7)
        virtual_pieceCount = self.pieceCount
        col = self.minimax(virtual_pieceCount, -sys.maxint-1, sys.maxint)
        #print('Column = %d' % col)
        result = self.playPiece(col)
        
        print('\n\nmove %d: Player %d, column %d\n' % (self.pieceCount, self.currentTurn, col+1))
        if self.currentTurn == 1:
            self.currentTurn = 2
        elif self.currentTurn == 2:
            self.currentTurn = 1