import arcade


# Main player entity class
class Player(arcade.Sprite):
    """
    Override to the Sprite class to provide additional functionality for animations
    (mostly just to override the update_animation() function)
    """
    def __init__(self):
        """
        Constructor for the AnimatedPlayerSprite class. Essentially sets up the needed state to
        support animations.

        Args:
            self (AnimatedPlayerSprite): The particular instance of the AnimatedPlayerSprite class
        """
        # Call the default sprite class so we get all that functionality
        super().__init__()

        # Counter to keep track of animation frames
        self.counter = 0
        # 0 is for moving right and 1 is for moving left
        self.direction = 0

        self.scale = 1.5

        # Load sprite animation textures
        self.idle_right_textures = []
        for i in range(4):
            texture = arcade.load_texture(f"textures/frames/knight_m_idle_anim_f{i}.png")
            self.idle_right_textures.append(texture)

        self.idle_left_textures = []
        for i in range(4):
            texture = arcade.load_texture(f"textures/frames/knight_m_idle_anim_f{i}.png", mirrored=True)
            self.idle_left_textures.append(texture)

        self.moving_right_textures = []
        for i in range(4):
            texture = arcade.load_texture(f"textures/frames/knight_m_run_anim_f{i}.png")
            self.moving_right_textures.append(texture)

        self.moving_left_textures = []
        for i in range(4):
            texture = arcade.load_texture(f"textures/frames/knight_m_run_anim_f{i}.png", mirrored=True)
            self.moving_left_textures.append(texture)

        # Assign a starting texture
        self.texture = self.idle_right_textures[0]

        # Adjust the hit box so it's not completely terrible
        self.points = [[-12.0, -19.0], [12.0, -19.0], [12.0, 15.0], [-12.0, 15.0]]

    def update_animation(self, delta_time: float = 2/60):
        """
        Override function that provides the functionality to update animation frames.

        Args:
            self (AnimatedPlayerSprite): The particular instance of the AnimatedPlayerSprite class.
            delta_time (float): Optional parameter that specifies the time passed (used to control frame rate)
        """
        self.counter += 1
        if self.counter > 3:
            self.counter = 0

        if self.change_x > 0 or self.change_y > 0:
            self.direction = 0
            self.texture = self.moving_right_textures[int(self.counter)]
        elif self.change_x < 0 or self.change_y < 0:
            self.direction = 1
            self.texture = self.moving_left_textures[int(self.counter)]
        else:
            if self.direction == 0:
                self.texture = self.idle_right_textures[int(self.counter)]
            else:
                self.texture = self.idle_left_textures[int(self.counter)]
