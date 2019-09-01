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
        self.player_deflection_angles = [300, 340, 20, 60]

        # Generate circle for more accurate collision detection
        self.circle_color = (0,255,0)
        self.circle_x = int(self.x + self.width / 2)
        self.circle_y = int(self.y + self.height / 2)
        self.circle_radius = int(self.width/2)
        self.collision_coordinates = self.get_collision_coordinates()

        # Add the sphere to the spheres list
        Sphere.sphere_list.append(self)

    def move(self):
        move_x = self.speed_x * math.sin(self.radians)
        move_y = self.speed_y * math.cos(self.radians)
        self.x += move_x
        self.circle_x += move_x
        self.y += move_y
        self.circle_y += move_y
        return

    # Get 8 (x,y) coordinates on the circle for more accurate collision 
    # detection. The first 4 are where the circle crosses the x/y axes. The 
    # second 4 are calculated by taking the sin and cos at 45 degree angles
    # from the center of the circle (distance is the radius).
    # coords = [top, bottom, left, right, topright, bottomright, bottomleft, topleft]
    def get_collision_coordinates(self):
        # Add the 4 coordinates on the x/y axes
        coords = []
        coords.append([self.circle_x, self.circle_y - self.circle_radius])
        coords.append([self.circle_x, self.circle_y + self.circle_radius])
        coords.append([self.circle_x - self.circle_radius, self.circle_y])
        coords.append([self.circle_x + self.circle_radius, self.circle_y])
        # Add the 4 different 45 degree (x,y) coordinates
        angle = 45
        right_angle = 90
        for i in range(4):
            radians = math.radians(angle)
            x = self.circle_x + (self.circle_radius * (math.cos(radians)))
            y = self.circle_y + (self.circle_radius * (math.sin(radians)))
            coords.append([x,y])
            angle += right_angle
        # Round all the coordinates to the nearest pixel
        for coord in coords:
            coord[0] = int(coord[0])
            coord[1] = int(coord[1])
        return coords

    def block_collision(self):
        return


def update(game, player, spheres):
    for sphere in spheres:
        if (game.level.sphere_edge_collision(game, sphere)):
            Sphere.sphere_list.remove(sphere)
            # TODO add what happens when sphere goes off bottom
            continue
        if (game.level.block_collision(sphere, game)):
            sphere.block_collision()
        player.player_sphere_collision(sphere)
        sphere.move()
    return