import pygame
from start_screen import StartScreen
from game import Game


def main():
    pygame.init()
    pygame.display.set_caption("PLATFORMER GAME: HELP")

    # Show the start screen and get player name
    start_screen = StartScreen()
    player_name = start_screen.display()

    # Start the game with the given player name
    game = Game(player_name)
    game.start_game()


if __name__ == "__main__":
    main()
