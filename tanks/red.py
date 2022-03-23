import arcade
import math
from constants import *

class Red_Tank(arcade.Sprite):
    def __init__(self,window):
        super().__init__("red.png", 0.12)
        self.active = True
        self.angle = 180
        self.shots = 0
        self.window = window
    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x, self.center_y + 50, 50, 15, (255, 255, 255), 1)
        indent = self.shots*10
        arcade.draw_rectangle_filled(self.center_x-indent/2, self.center_y + 50, 50-indent, 13, (255, 165, 0))

    def update(self):
        hits = arcade.check_for_collision_with_list(self, self.window.projectiles)
        for bullete in hits:
            bullete.kill()
            self.shots += 1
        if self.shots >= 5:
            self.texture = arcade.load_texture("red_broken.png")
            self.shots = 5