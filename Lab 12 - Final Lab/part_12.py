import arcade

# Constants
SPRITE_SCALING_PIN = 0.5
SPRITE_SCALING_BALL = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Test")

        # Sprite Lists
        self.ball_list = None
        self.pin_list = None

        # Physics Engine
        self.physics_engine = None

    def setup(self):
        arcade.set_background_color(arcade.color.FRENCH_BEIGE)

        self.ball_list = arcade.SpriteList()
        self.pin_list = arcade.SpriteList()

        self.score = 0

        # Creating the ball
        # Ball png is from Kenney.nl/assets/sports-pack
        self.ball_sprite = arcade.Sprite("images/ball_bowling1.png", SPRITE_SCALING_BALL)
        self.ball_sprite.center_x = 50
        self.ball_sprite.center_y = 64
        self.ball_list.append(self.player_sprite)

        # Creating Pins
        # Pin png is from pngkey.com/pngs/bowling-pin/
        pin = arcade.Sprite("images/bowling_pin.png", SPRITE_SCALING_PIN)
        pin.center_x = 300
        pin.center_y = 200
        self.pin_list.append(pin)

        # # --- Place pins inside a loop
        # for x in range(173, 650, 64):
        #     pin = arcade.Sprite("images/bowling_pin.png", SPRITE_SCALING_PIN)
        #     pin.center_x = x
        #     pin.center_y = 350
        #     self.pin_list.append(pin)

        # --- Place pins with a list
        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            pin = arcade.Sprite("images/bowling_pin.png", SPRITE_SCALING_PIN)
            pin.center_x = coordinate[0]
            pin.center_y = coordinate[1]
            self.pin_list.append(pin)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.ball_sprite, self.pin_list)

    def on_draw(self):
        arcade.start_render()
        self.pin_list.draw()
        self.ball_list.draw()

    def update(self, delta_time):
        self.physics_engine.update()

    # def on_key_press(self, key, modifiers):
    #     """Called whenever a key is pressed. """
    #
    #     if key == arcade.key.UP:
    #         self.player_sprite.change_y = MOVEMENT_SPEED
    #     elif key == arcade.key.DOWN:
    #         self.player_sprite.change_y = -MOVEMENT_SPEED
    #     elif key == arcade.key.LEFT:
    #         self.player_sprite.change_x = -MOVEMENT_SPEED
    #     elif key == arcade.key.RIGHT:
    #         self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball_sprite.change_x = 0

    def main():
        """ Main method """
        window = MyGame()
        window.setup()
        arcade.run()

    if __name__ == "__main__":
        main()