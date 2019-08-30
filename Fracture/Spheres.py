import pygame
import math


import random


class Sphere:
    sphere_list = []
    def __init__(self, game):
        self.image = game.sphere
        self.speed = 5
        self.degree_direction = random.randint(10,80)
        self.width, self.height = game.get_image_size(self.image)
        self.x = 100.0
        self.y = game.screen_height - 100.0
        self.right = True
        self.left = False
        self.up = True
        self.down = False
        self.player_deflection_angles = [280, 300, 320, 340, 20, 40, 60, 80]
        Sphere.sphere_list.append(self)


def edge_collision(game, sphere, radians):
    # Right Border
    speed = sphere.speed * math.sin(radians)
    x_position = sphere.x + sphere.width + speed
    if (x_position >= game.screen_width):
        sphere.right = False
        sphere.left = True
    # Left Border
    x_position = sphere.x - sphere.width - speed
    if (x_position <= 0):
        sphere.right = True
        sphere.left = False

    speed = sphere.speed * math.cos(radians)
    # Top Border
    y_position = sphere.y - sphere.width - speed
    if (y_position <= 0):
        sphere.up = False
        sphere.down = True
    # Bottom Border
    y_position = sphere.y + sphere.height + speed
    if (y_position >= game.screen_height):
        sphere.up = True
        sphere.down = False
        #Sphere.sphere_list.remove(sphere)
        # TODO add result for missing a sphere
    return

def object_collision():
    # TODO add object collision
    return

def move_sphere(sphere, radians):
    # Sphere moving left/right
    speed = sphere.speed * math.sin(radians)
    if (speed < 0):
        speed *= -1
    if (sphere.right):
        sphere.x += speed
    if (sphere.left):
        sphere.x -= speed
    # Sphere moving up/down
    speed = sphere.speed * math.cos(radians)
    if (speed < 0):
        speed *= -1
    if (sphere.up):
        sphere.y -= speed
    if (sphere.down):
        sphere.y += speed
    return

def get_deflection_degree(sphere, player, player_segments): # TODO refine x check
    # Player image _______________________________
    #             [___|___|___|___|___|___|___|___]
    # Segments      1   2   3   4   5   6   7   8
    segment_position = 1
    for segment in player_segments:
        seg_start = math.floor(segment[0])
        if (segment_position == 1):
            seg_start -= sphere.width
        if (segment_position == 8):
            seg_end += sphere.width / 2
        seg_end = math.ceil(segment[1])
        floor_x = math.floor(sphere.x)
        if (floor_x >= seg_start and floor_x <= seg_end):
            length = len(player_segments)
            for i in range(1, length + 1):
                if (i == segment_position):
                    if (sphere.left):
                        return sphere.player_deflection_angles[length-i]
                    else:
                        return sphere.player_deflection_angles[i-1]
        segment_position += 1
    return 0

def player_collision(sphere, player):
    sphere.up = True
    sphere.down = False
    player_segments = player.get_player_segments()
    sphere.degree_direction = get_deflection_degree(sphere, player, player_segments)
    return

def update(game, player, spheres):
    for sphere in spheres:
        radians = math.radians(sphere.degree_direction)
        if (sphere.down):
            if (player.sphere_collision(sphere)):
                player_collision(sphere, player)
        elif (object_collision(sphere, game)):
            print("object collision")
        move_sphere(sphere, radians)
        edge_collision(game, sphere, radians)
    return