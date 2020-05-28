"""
Main game function
"""
import arcade

from Player import Player
from map_generation.game_map import GameMap
from game_objects.GameObject import GameObject

VERSION = "0.0.1"
SCREEN_TITLE = "MagiQuest | v0.0.1"
GAME_SPEED = 4/60

ROW_COUNT = 45
COLUMN_COUNT = 45

WIDTH = 16
HEIGHT = 16

MARGIN = 0

# Figure out screen size based on the tile size
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MagiQuest(arcade.Window):
    """
    Main entry point of the entire program
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title, update_rate=GAME_SPEED)

        arcade.set_background_color(arcade.color.PURPLE)

        # Define all the needed player properties
        self.player = GameObject(texture_id=10)

        # Define all the sprite lists
        self.floor = arcade.SpriteList()
        self.obs = arcade.SpriteList()
        self.items = arcade.SpriteList()
        self.enemies = arcade.SpriteList()

        self.grid_sprites = arcade.SpriteList()

        self.engine = None

        self.map = None

    def setup(self):
        self.map = GameMap(COLUMN_COUNT, ROW_COUNT)
        self.map.make_map(level=1)

        for row in range(COLUMN_COUNT):
            for column in range(ROW_COUNT):
                x = column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
                y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)

                sprite = None

                if self.map.tiles[row][column] == 0:
                    sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, arcade.color.WHITE)
                elif self.map.tiles[row][column] == 1:
                    sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, arcade.color.BLACK)
                elif self.map.tiles[row][column] == 22:
                    sprite = self.player

                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprites.append(sprite)



    def resync_grid_with_sprites(self):
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # We need to convert our two dimensional grid to our
                # one-dimensional sprite list. For example a 10x10 grid might have
                # row 2, column 8 mapped to location 28. (Zero-basing throws things
                # off, but you get the idea.)
                # ALTERNATIVELY you could set self.grid_sprite_list[pos].texture
                # to different textures to change the image instead of the color.
                pos = row * COLUMN_COUNT + column
                if self.grid[row][column] == 0:
                    self.grid_sprite_list[pos].color = arcade.color.WHITE
                else:
                    self.grid_sprite_list[pos].color = arcade.color.GREEN

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below

        self.grid_sprites.draw()

        #self.player.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.W:
            self.player.change_y = 8
        elif key == arcade.key.S:
            self.player.change_y = -8
        elif key == arcade.key.A:
            self.player.change_x = -8
        elif key == arcade.key.D:
            self.player.change_x = 8

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.W:
            self.player.change_y = 0
        elif key == arcade.key.S:
            self.player.change_y = 0
        elif key == arcade.key.A:
            self.player.change_x = 0
        elif key == arcade.key.D:
            self.player.change_x = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MagiQuest(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
