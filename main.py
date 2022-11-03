from random import randint
from tic_tac_toe import TicTacToe

mode = input("\nWelcome to Tic Tac Toe game.\nEnter 'S' for Single Player Mode & 'M' for Multiplayer Mode:     ")

game  = TicTacToe()

if mode == "S":
    print("\nYou will be player 'X'.")
    users_marker, computers_marker = "X", "O"
    users_turn_done = computers_turn_done = game.turn
    while not game.game_complete and not game.game_over():
        users_block_loc = input("\nChoose the block to place your Marker 'X', for top left block block enter '0,0':     ").split(",")
        while not users_turn_done(loc=users_block_loc, marker=users_marker):
            users_block_loc = input("\nChoose the block to place your Marker 'X', for top left block block enter '0,0':     ").split(",")
        if not game.game_over():
            computers_block_loc = [randint(0, 2), randint(0, 2)]
            while not computers_turn_done(loc=computers_block_loc, marker=computers_marker):
                computers_block_loc = [randint(0, 2), randint(0, 2)]
        
elif mode == "M":
    print("\nPlayer one will be 'X' and Player two will be 'O'.")
    player1_marker, player2_marker = "X", "O"
    player1_turn_done = player2_turn_done = game.turn
    while not game.game_over():
        player1_block_loc = input("\nChoose the block to place your Marker 'X', for top left block block enter '0,0':     ").split(",")
        while not player1_turn_done(loc=player1_block_loc, marker=player1_marker):
            player1_block_loc = input("\nChoose the block to place your Marker 'X', for top left block block enter '0,0':     ").split(",")
        if not game.game_over():
            player2_block_loc = input("\nChoose the block to place your Marker 'O', for top left block block enter '0,0':     ").split(",")
            while not player2_turn_done(loc=player2_block_loc, marker=player2_marker):
                player2_block_loc = input("\nChoose the block to place your Marker 'O', for top left block block enter '0,0':     ").split(",")

else:
    print("Invlid input for mode selection.")