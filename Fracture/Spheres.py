import pygame
import math


import random


class Sphere:
    sphere_list = []
    def __init__(self, game):
        self.image = game.sphere
        self.speed_x = 5
        self.speed_y = -self.speed_x
        self.width, self.height = game.get_image_size(self.image)
        self.angle = random.randint(5,85)
        self.radians = math.radians(self.angle)
        self.x = game.screen_width / 2
        self.y = game.screen_height / 2
        self.player_deflection_angles = [290, 330, 30, 70]

        # Generate circle for more accurate collision detection
        self.circle_color = (0,255,0)
        self.circle_x = int(self.x + self.width / 2)
        self.circle_y = int(self.y + self.height / 2)
        self.circle_radius = int(self.width/2)

        # Add the sphere to the spheres list
        Sphere.sphere_list.append(self)


#def edge_collision(game, sphere, radians):
def edge_collision(game, sphere):
    x = sphere.circle_x
    y = sphere.circle_y
    radius = sphere.circle_radius
    if (x < radius or x > game.screen_width - radius):
        sphere.speed_x *= -1
    if (y < radius):
        sphere.speed_y *= -1
    if (y > game.screen_height - radius):
        Sphere.sphere_list.remove(sphere)
    return

def move_sphere(sphere):
    move_x = sphere.speed_x * math.sin(sphere.radians)
    move_y = sphere.speed_y * math.cos(sphere.radians)
    sphere.x += move_x
    sphere.circle_x += move_x
    sphere.y += move_y
    sphere.circle_y += move_y
    return

def block_collision(sphere, radians):
    return

def get_segment_position(sphere, player_segments):
    x = sphere.circle_x
    segment_position = 1
    for segment in player_segments:
        x_start = math.floor(segment[0])
        x_end = math.ceil(segment[1])
        if (x >= x_start and x <= x_end):
            break
        segment_position += 1
    return segment_position

#def player_deflect(sphere, player, player_segments): # TODO refine x check
#    # Player image _______________________________
#    #             [_______|_______|_______|_______]
#    # Segments        1       2       3       4
#    segment_position = get_segment_position(sphere, player_segments)
#    index = segment_position - 1
#    sphere.angle = sphere.player_deflection_angles[index]
#    sphere.radians = math.radians(sphere.angle)
#    if (sphere.radians < 0):
#        sphere.radians *= -1
#    sphere.speed_y *= -1
#    return

def player_collision(sphere, player):
    player_segments = player.get_player_segments()
    #player_deflect(sphere, player, player_segments)
    sphere.speed_y *= -1
    return

def update(game, player, spheres):
    for sphere in spheres:
        if (player.sphere_collision(sphere)):
                player_collision(sphere, player)
        #if (game.level.check_block_collision(sphere, game)):
        #    block_collision(sphere, radians)
        move_sphere(sphere)
        edge_collision(game, sphere)
    return