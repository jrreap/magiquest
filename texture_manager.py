import arcade


class _TextureManager:
    FLOOR = arcade.load_texture("textures/frames/floor_1.png")
    WALL = arcade.load_texture("textures/frames/wall_mid.png")


TILES = _TextureManager
