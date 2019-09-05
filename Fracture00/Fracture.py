import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
import game_classes


#####################
#    Game Handler   #
#####################
def play_game(game):
    for i in range(1):
        game_classes.Sphere(game)
    player = game_classes.Player(game)
    while (game.continue_game()):
        spheres = game_classes.Sphere.sphere_list
        game.draw_game(player, spheres)
        for sphere in spheres:
            sphere.update(game, player)
        player.get_player_movement(game)
    return


#####################
#        Main       #
#####################
def main():
    game = game_classes.Game()

    #game.title_screen()
    play_game(game)
    Events.quit_game()


if __name__ == "__main__":
    main()