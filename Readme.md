# Description
This is a connect4 game with an AI agent as a computer. 

# Game Modes
## a. Interactive
In the interactive mode, the game should run from the command line with the following arguments
    python maxconnect4.py interactive [input-file] [computer-next/human-next] [depth]
1. Argument [inputfile] - file containing the initial board state.This way we can start the program from a non-empty board state. If the input file does not exist, the program should just create an empty board state and start again from there.
2. Argument [computer-next/human-next] specifies whether the computer should make the next move or the human. 
3. Argument [depth] specifies the number of moves in advance that the computer should consider while searching for its next move. In other words, this argument specifies the depth of the search tree. Essentially, this argument will control the time takes for the computer to make a move.

In this mode, the user can play against the AI Agent. 

## b. One-Move Mode
The purpose of the one-move mode is to make it easy for programs to compete against each other, and communicate their moves to each other using text files. The one-move mode is invoked as follows:
    python maxconnect4 one-move [input_file] [output_file] [depth]