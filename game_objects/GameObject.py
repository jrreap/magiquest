"""
A wrapper of the Sprite class that adds additional values for the game
"""

import arcade
import os


class GameObject(arcade.Sprite):
    def __init__(
            self,
            x: int = 0,
            y: int = 0,
            name=None,
            blocks=False,
            texture_id: int = 0
    ):
        super().__init__(scale=1)

        self._x = 0
        self._y = 0
        self._texture_id = 0

        self.texture = arcade.load_texture("textures/frames/ui_heart_full.png")

        self.x = x
        self.y = y

        self.name = name

        self.blocks = blocks

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self.center_x = self._x * 16 + 16 / 2

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self.center_y = self._y * 16 + 16 / 2
